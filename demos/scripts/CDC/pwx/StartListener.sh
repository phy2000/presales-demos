echo on
echo '>>>>>>>>>>>>>>>' $(date) >> listener.out
nohup dtllst node1 >> listener.out &
