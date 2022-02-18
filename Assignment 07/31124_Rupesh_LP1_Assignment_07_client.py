# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 07

import random
import socket,datetime
import sys
import threading
import time

host="192.168.43.233"
port=9999
s=socket.socket()

s.connect((host,port))

def request_for_time(t):
    s.send(str.encode(t))
    data = str(s.recv(1024),"utf-8")
    if len(data) and t=="ntp":
        t1,t2=map(int,data.split())
        return t1,t2
    if len(data) and t=="lamport":
        msg,t = data.split()
        return msg,int(t)
    return False


class ClockSync:
    def __init__(self):
        self.my_time=datetime.datetime.now().timestamp()
    def ntp(self):
        time_offset=float('inf')
        round_trip=float('inf')
        d=datetime.datetime
        print("t0          t1          t2          t3          T          offset round_trip")
        while time_offset>1:
            t0=int(self.my_time)
            t1,t2=request_for_time("ntp")
            time.sleep(0.723 * random.randint(0, 4))
            t3=int(d.now().timestamp())
            time_offset=abs(((t1-t0)+(t2-t3))/2)
            round_trip=(t3-t0)-(t2-t1)
            self.my_time=int(t2+round_trip/2)
            print(f"{str(t0).ljust(12)}{str(t1).ljust(12)}{str(t2).ljust(12)}{str(t3).ljust(12)}{str(self.my_time).ljust(12)}{time_offset}   {round_trip}")
        print(f"synced to:  {self.my_time}\n")

    def time_counter(self):
        while True:
            self.timer+=1
            time.sleep(1.05)
            if self.timer<0:
                return
    def lamport(self):
        self.timer=int(self.my_time)
        thread_1=threading.Thread(target=self.time_counter)
        thread_1.start()
        print("t0\t\t\ttr\t\t\ttf")
        for _ in range(4):
            msg,t=request_for_time("lamport")
            print(f"{self.timer}\t{t}\t",end="")
            self.timer=max(self.timer,t)+1
            print(f"{self.timer}")
        self.my_time=self.timer
        print(f"synced to:  {self.my_time}")
        self.timer*=-1


clocksync=ClockSync()
print("NTP: ")
clocksync.ntp()
print("Lamport: ")
clocksync.lamport()
s.send(str.encode("q"))
s.close()
sys.exit()