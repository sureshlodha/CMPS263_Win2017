"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We analyze the data of H-1B_FY16.csv in the script.

Author:
Ran Xu
rxu3@ucsc.edu

"""
import psycopg2
import sys,csv

#Define our connection string
conn_string = "host='localhost' dbname='postgres' user='ranxu' password='123456'"

# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cur = conn.cursor()
print "Connected!\n"

cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
conn.commit()
tnames = []
for tname in cur.fetchall():
	tnames.append(tname[0])
print tnames

# Constructing commands
commands = []
prefix = 'drop table '
for tname in tnames:
	commands.append(prefix + tname)

# Drop all existing tables
print "\nStart dropping all tables"
for command in commands:
	print '\nExecuting commands......'
	print command
	cur.execute(command)
	conn.commit()



#creating table
commands = ('''
	CREATE TABLE H1B_16(
		CASE_NUMBER varchar(20),
		CASE_STATUS varchar(20),
		VISA_CLASS varchar(200),
		EMPLOYER_NAME varchar(200),
		JOB_TITLE varchar(200),
		TOTAL_WORKERS integer,
		WORKSITE_CITY varchar(200),
		WORKSITE_COUNTY varchar(50),
		WORKSITE_STATE varchar(20),
		PREVAILING_WAGE money
		);
	''',
	'''
	CREATE TABLE temp(
		CASE_NUMBER varchar(20),
		CASE_STATUS varchar(20),
		CASE_SUBMITTED date,
		DECISION_DATA date,
		VISA_CLASS varchar(200),
		EMPLOYMENT_START_DATA date,
		EMPLOYMENT_END_DATE date,
		EMPLOYER_NAME varchar(200),
		EMPLOYER_ADDRESS varchar(200),
		EMPLOYER_CITY varchar(200),
		EMPLOYER_STATE varchar(200),
		EMPLOYER_POSTAL_CODE varchar(20),
		EMPLOYER_COUNTRY varchar(200),
		EMPLOYER_PROVINCE varchar(200),
		EMPLOYER_PHONE varchar(50),
		EMPLOYER_PHONE_EXT varchar(20),
		AGENT_ATTORNEY_NAME varchar(200),
		AGENT_ATTORNEY_CITY varchar(200),
		AGENT_ATTORNEY_STATE varchar(50),
		JOB_TITLE varchar(200),
		SOC_CODE varchar(20),
		SOC_NAME varchar(200),
		NAIC_CODE integer,
		TOTAL_WORKERS integer,
		FULL_TIME_POSITION varchar(20),
		PREVAILING_WAGE money,
		PW_UNIT_OF_PAY varchar(50),
		PW_WAGE_SOURCE varchar(50),
		PW_SOURCE_YEAR integer,
		PW_SOURCE_OTHER varchar(200),
		WAGE_RATE_OF_PAY_FROM money,
		WAGE_RATE_OF_PAY_TO money,
		WAGE_UNIT_OF_PAY varchar(20),
		H1B_DEPENDENT varchar(20),
		WILLFUL_VOILATOR varchar(50),
		WORKSITE_CITY varchar(200),
		WORKSITE_COUNTY varchar(50),
		WORKSITE_STATE varchar(20),
		WORKSITE_POSTAL_CODE varchar(20),
		ORIGINAL_CERT_DATE date
		);
	''',
	'''
		CREATE TABLE STATE(
		STATES varchar(20),
		ABB varchar(20)
		);
	''')
for command in commands:
	print '\nExecuting commands......'
	print command
	cur.execute(command)
	conn.commit()

with open('../datasource/H-1B_FY16.csv') as f:
	cur.copy_expert('''COPY temp FROM STDIN DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f)
f.close()

with open('../datasource/States_Abb.csv') as f:
	cur.copy_expert('''COPY STATE FROM STDIN DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f)
f.close()

commands2=(

	#only select certain columns that we care most.
	'''
	INSERT INTO H1B_16(CASE_NUMBER,CASE_STATUS,VISA_CLASS,EMPLOYER_NAME,JOB_TITLE,TOTAL_WORKERS,WORKSITE_CITY,WORKSITE_COUNTY,WORKSITE_STATE,PREVAILING_WAGE)
	SELECT CASE_NUMBER,CASE_STATUS,VISA_CLASS,EMPLOYER_NAME,JOB_TITLE,TOTAL_WORKERS,WORKSITE_CITY,WORKSITE_COUNTY,WORKSITE_STATE,PREVAILING_WAGE FROM  temp;
	''',
	'''
	DELETE FROM H1B_16
	WHERE VISA_CLASS!='H-1B';
	''',
	#get the work state, and the total workers in each state, in each
	'''
	CREATE TABLE Groupby_worksite AS
	SELECT WORKSITE_STATE,COUNT(CASE_NUMBER) AS COUNT_WORKERS
	FROM H1B_16
	GROUP BY WORKSITE_STATE ORDER BY COUNT_WORKERS;
	''',
	#
	'''
	CREATE TABLE workers_states AS SELECT STATES, ABB, COUNT_WORKERS FROM STATE LEFT JOIN Groupby_worksite ON STATE.ABB=Groupby_worksite.WORKSITE_STATE ORDER BY COUNT_WORKERS DESC;
	''',

	#ANALYSIS OF THE STATUS IN EACH EMPLOYER, BY JOINNING OF TWO FOLLOWING TABLES, WE CAN GET THE RATIO OF CERTIFIED H1B IN EACH EMPLOYER
	'''
	CREATE OR REPLACE FUNCTION emp_state(state text) RETURNS TABLE (EMPLOYER varchar(200), NUM_WORKERS bigint) AS
	$$ BEGIN RETURN QUERY SELECT H1B_16.EMPLOYER_NAME, COUNT(CASE_NUMBER) AS SUM_TOTAL_WORKERS FROM H1B_16 WHERE H1B_16.WORKSITE_STATE=state GROUP BY EMPLOYER_NAME ORDER BY SUM_TOTAL_WORKERS DESC; END;$$
	LANGUAGE 'plpgsql';
	''',



)
for command in commands2:
	print '\nExecuting commands......'
	print command
	cur.execute(command)
	conn.commit()


#create the 50 files of the US 50 state, with all the companies in each state
with open('../datasource/States_Abb.csv','r') as f2:
	reader = csv.reader(f2)
	#print reader
	#reader.next()
	reader.next()
	for row in reader:

		state_name=row[1]
		#print state_name
		cur.execute('''CREATE TABLE %s AS SELECT * FROM emp_state('%s')'''%(state_name+'_workers',state_name))
		conn.commit()
		with open('../output/viz/H1B_Companies/'+state_name+'.csv','w') as f3:
			cur.copy_expert('''COPY %s to STDOUT DELIMITER ',' CSV HEADER encoding 'windows-1251';'''%(state_name+'_workers'),f3)
		f3.close()
f2.close()

with open('../output/viz/H1B_Companies/state_count_workers.csv','w') as f4:
	cur.copy_expert('''COPY workers_states to STDOUT DELIMITER ',' CSV HEADER encoding 'windows-1251';''',f4)
f4.close()

print '\nAll commands executed'

conn.close()
print '\nClosed connection to databsed'
