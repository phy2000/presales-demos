#!/usr/bin/env /usr/bin/python
import threading
from random import randint
from math import exp
from datetime import datetime
import time

from kafka import KafkaProducer

NumPub=10
NumLinePerPub=4
Tfreeze=-10   # Cooler min temperatur
Tlow=3        # Beer min target Temp
Thigh=7	      # Beer max target Temp
Tcrit=11      # Beer critical temperature
Troom=21      # Room temperature
t_halfw=500   # half worth time on warming 
t_halfc=800   # half worth time on cooling
t_step=2      # avg time step length
t_failure=300 # pub_1 fails to cool
kegSizes=[10, 20, 50, 100] # Array of keg size
maxRunTimeS=1800
maxRunEvents=20 #Run script for maxRunEvents (ignored if zero)
events_count=0 

def do_work(pub_id, line_id, stop):
    global events_count
    # print "Pub %2d Line %2d"% (pub_id,line_id)
    # choose state random 0=warmin, 1=cooling
    producer = KafkaProducer(bootstrap_servers='quickstart:9192')# ,localhost:19092,localhost:29092,localhost:39092')
    state=randint(0,1) # 0 off, 1 = on
    my_t_step=randint(1,2*t_step)       # random time steps
    my_kegSize=kegSizes[randint(0,3)]
    my_remaining_l=my_kegSize
    Tstart=randint(Tlow*100,Thigh*100+1)/100.0 # random start temperature
    t_start=time.time()
    t_int_start=t_start
    t_last_switch=t_int_start
    pint_dispersed=0
    if(pub_id==1): # ensure that pub_id 1 has heighest despense
	state=1
	my_kegSize=100
	my_remaining_l=my_kegSize
	my_t_step=2
    hpint_dispersed=0
    print "Pub %2d Line %2d Tstart=%7.4f, t_step=%d, kegSize=%d"% (pub_id,line_id, Tstart,my_t_step,my_kegSize)
    while True:
       events_count=events_count+1
       now=time.time();
       t_int=now-t_int_start
       # Compute remaining l
       my_remaining_l=my_remaining_l-pint_dispersed*0.473176-hpint_dispersed*0.473176/2
       # If negative we have opened a new keg
       if (my_remaining_l<0):
          my_remaining_l=my_remaining_l+my_kegSize

       if(state==1):
          T=Tfreeze+(Tstart-Tfreeze)*exp(-t_int*1.0/t_halfc) 
	  if(T<Tlow):
              # print "%5.2f < Tlow=%5.2f, switch off" % (T, Tlow)
              state=0
              t_int_start=now
              Tstart=T
       else:
          T=Troom+(Tlow-Troom)*exp(-t_int*1.0/t_halfw) 
	  if(T>Thigh):
              # print "%5.2f > Thigh=%5.2f, switch off" % (T, Thigh)
              if (not (pub_id==1 and (now - t_start) > t_failure)):
                 state=1
                 t_int_start=now
                 Tstart=T
       kegPressure=randint(800,1100)/100.0
       tabPressure=randint(900,950)/1000.0*kegPressure;
       Ttab=T+randint(5,100)/50.0
       dttm_str=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
       line="%s %4d %4d %4.1f %5.2f %4.1f %5.2f %d %d %6.3f" % (dttm_str, pub_id, line_id, T, kegPressure, Ttab, tabPressure, pint_dispersed, hpint_dispersed, my_remaining_l)
       json="{\"tstamp\":\"%s\", \"pubID_int\":%d, \"lineID_int\":%d, \"kegTemp_C\":\"%5.2f\", \"kegPressure_PSI\":\"%4.1f\", \"tapTemp_C\":\"%5.2f\", \"tapPressure_PSI\":\"%4.1f\", \"tapTotDispensed_HPints_int\":%d, \"tapTotDispensed_Pints_int\":%d, \"kegRemainingVol_lit\":\"%7.3f\"}" % (dttm_str, pub_id, line_id, T, kegPressure, Ttab, tabPressure, pint_dispersed, hpint_dispersed, my_remaining_l)
       #print json
       #print line
       producer.send('beerReadings', json)
       #producer.send('one2one_in', json)

       # Dispesing is weighted by kegsize and time interval 
       pint_dispersed=randint(0,max(my_kegSize*my_t_step/50,1))
       hpint_dispersed=randint(0,max(my_kegSize*my_t_step/50,1))
       # No disperse if beer too warm
       if(T>Tcrit):
             print "pub_id=%d line_id=%s T=%5.2f too warm!" % (pub_id, line_id, T)
             pint_dispersed=0
             hpint_dispersed=0
       #print "  - Event (%d) sent." % (events_count)
       #if events_count == maxRunEvents:
       #       print "  Max number of events (%d) reached. Exiting loop." % (events_count)
       #       break  
       if stop():
              print("  Exiting loop.")
              break
       time.sleep(my_t_step)
      
    print "Thread pubid %d line %d  signing off" % (pub_id, line_id)


def main():
    stop_threads = False
    workers = []
    for pub_id in range(NumPub):
        if (pub_id==0): # max pubId 0 bestselling
          thisMaxLineId=NumLinePerPub
        else:
	  thisMaxLineId=randint(1,NumLinePerPub) # other get random
        for line_id in range(thisMaxLineId):
#	    print "Pub %d Line%d" % (pub_id+1, line_id+1)
            tmp = threading.Thread(target=do_work, args=(pub_id+1, line_id+1, lambda: stop_threads))
            workers.append(tmp)
            tmp.start()
    time.sleep(maxRunTimeS)
    print('main: done sleeping; time to stop the threads.')
    stop_threads = True
    for worker in workers:
        worker.join()
    print('Finished.')
    print "Events Count= %2d"% (events_count)

if __name__ == '__main__':
    main()
