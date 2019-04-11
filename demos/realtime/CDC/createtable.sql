CONNECT / AS SYSDBA;     

--
-- For testing, create an IVP table
--
CREATE TABLE cdctest.cdctest 
(keystring VARCHAR2(100) NOT NULL ENABLE, 
 count NUMBER(5),
 tstamp VARCHAR2(100), 
 numfield NUMBER(5),
 vcharfield VARCHAR2(100),
 PRIMARY KEY (keystring), 
 SUPPLEMENTAL LOG DATA (ALL) COLUMNS);

INSERT INTO cdctest.cdctest VALUES ('keystring',1,'tstamp', 1, 'vcharfield');

COMMIT;
