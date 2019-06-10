#! /usr/bin/python3
import datetime
name=input("enter your name --")
datetime=datetime.datetime.now()
c_time=datetime.hour
 if c_time>=5 and c_time<12:
     print("GOOD MORNING !!!! "+str(name))
 elif c_time>=12 and c_time<16:
     print("GOOD AFTERNOON !!! "+str(name))
 elif c_time>=16 and c_time<22:
     print("GOOD EVENING !!! "+str(name))
 elif c_time>=22 and c_time<5:
     print("GOOD NIGHT !!! "+str(name))

