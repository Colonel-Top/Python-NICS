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
ids = 1
elname = "blender"
eltype = "Kitchen Utilities"
initVALUE = 500
initNAME = "Tester"
times = 1

def main():
    print("Loading Database ...")
    fetch()
    Connection()
    Menu()
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
        sys.exit()
def clear_query():
    print(str(cur.execute("DELETE FROM `nics`;"))+ " Rows Affected")
    print("Query Cleared")
    db.commit()
    Menu()
def fetch():
    last_result = int(cur.execute("SELECT ID FROM `nics` ORDER BY ID DESC LIMIT 1"))
    #print(last_result)
    ids = cur.fetchone()
    if ids:
        ids = ids[0]
    else:
        ids = "None"
    print ("Last ID : " + str(ids))
    Menu()
def setup():
    print("Please Insert This following Information for Experiment")
    print("-------------------------------------------------------")
    global initNAME,elname,eltype,times
    initNAME = input("Name : ")
    elname = input("Electricity name : ")
    eltype = input("Electricity type : ")
    times = int(input("Count of Test : "))
    Menu()
def Send_toDB (times):
    last_result = int(cur.execute("SELECT ID FROM `nics` ORDER BY ID DESC LIMIT 1"))
    #print(last_result)
    ids = cur.fetchone()
    if ids:
        ids = int(ids[0])
    else :
        ids = int(0)
    ids =  ids +1
    print("Pushing Query ...")
    i = 0
    while(times > 0):
        i = i+1
        print("%s of %s",(i,times))
        push_query(ids,initNAME,elname,eltype,gdate, strtime, initVALUE)
        times -= 1
    Menu()
def push_query(ids,initNAME,elname,eltype,gdate, strtime, initVALUE):
    try:
        now = datetime.now()
        gdate = (now.strftime("%Y-%m-%d"))
        strtime = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        initVALUE = randint(0,1000)
        print ("PUSH VALUES : (%s,%s,%s,%s,%s,%s,%s)",( ids,initNAME,elname,eltype,gdate, strtime, initVALUE))
        cur.execute("INSERT INTO nics (ID,NAME,El_Name,EL_TYPE,DATE,TIME,VALUE) VALUES (%s,%s,%s,%s,%s,%s,%s)",( ids,initNAME,elname,eltype,gdate, strtime, initVALUE))
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
