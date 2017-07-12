#!/usr/bin/python
import time
import MySQLdb
import sys
from random import randint
#Date
from datetime import datetime
now = datetime.now()
gdate = (now.strftime("%Y-%m-%d"))
strtime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
db = MySQLdb.connect("pe.colonel-tech.com","colonel","pythonelectric","pe" )
cur = db.cursor()
#connection
def Connection():
    global db,cur
    db = MySQLdb.connect("pe.colonel-tech.com","colonel","pythonelectric","pe" )
    cur = db.cursor()
#define

initVALUE = 500
initNAME = "Tester"
times = 1

def main():
    print("Loading Database ...")
    Connection()
'''
def Menu():
    m_select = int(input("1. to Fetch last Row\n2.Set up\n3.Push Query with current Settings\n4.Clear Query\nElse Exirt\nEnter Number : "))
    if m_select == 1:
        fetch()
    elif m_select == 2:
        setup()
    elif m_select == 3:
        Send_toDB(times)
    elif m_select == 4:
        clear_query()
    else:
        print("Out of Choice Terminated Program")
        db.close()
        sys.exit()'''
def clear_query():
    print(str(cur.execute("DELETE FROM `nics`;"))+ " Rows Affected")
    print("Query Cleared")
    db.commit()
def fetch():
    last_result = int(cur.execute("SELECT Dayamount FROM `record` WHERE 1"))
    #print(last_result)
    ids = cur.fetchone()
    if ids:
        times = ids[0]
    else:
        times = 0
    print ("Total Day to measure : " + str(times))
def measurehour()
    totalrun = 3600
    while(totalrun >=0):
        
def Send_toDB (times):
    print("Pushing Query ...")
    i = 0
    while(times > 0):
        i = i+1
        #print("%s of %s",(i,times))
        push_query(gdate, strtime, initVALUE)
        times -= 1
def push_query(gdate, strtime, initVALUE):
    try:
        now = datetime.now()
        gdate = (now.strftime("%Y-%m-%d"))
        strtime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        initVALUE = randint(0,1000)
        print ("PUSH VALUES : (%s,%s,%s)",( gdate, strtime, initVALUE))
        cur.execute("INSERT INTO nics (DATE,TIME,VALUE) VALUES (%s,%s,%s)",(gdate, strtime, initVALUE))
        '''if cur.lastrowid:
            print('last insert id', cur.lastrowid)
        else:
            print('last insert id not found')'''
        db.commit()
    except Exception as e:
        print (e)
        db.rollback()
#INSERT INTO `nics`(`DATE`, `TIME`, `VALUE`) VALUES ("2017-07-05","22:11:00",250)
if __name__ == "__main__":
    main()
