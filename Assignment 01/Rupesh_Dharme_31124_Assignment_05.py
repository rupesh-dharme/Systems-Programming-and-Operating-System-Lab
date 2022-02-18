# Name: Rupesh Dharme
# Class: TE 01
# Batch: L1
# Roll no: 31124
# Assignment 05

# Problem statement:
#   Implementation of CPU Scheduling Algorithms: FCFS , SJF (Preemptive),
#   Priority (Non-Preemptive) and Round Robin (Preemptive)

import pandas as pd #representing tabular format
import numpy as np #creating arrays

class Process():
    def __init__(self, index, arrival, burst, priority):
        self.index = index
        self.arrival = arrival
        self.burst = burst
        self.t = burst #for round robins burst time remaining
        self.t1 = burst #for sjf
        self.t2 = burst #for sjf np
        self.priority = priority
        self.complete = False  # to mark a process completed

    def show(self):
        print("Process", self.index, "details:")
        print("Priority", self.priority)
        print("Arrival time (in seconds)", self.arrival)
        print("Burst time (in seconds)", self.burst)
        print()



#Start fcfs
def fcfs(l, interval): 
    l = sorted(l, key=lambda process: process.arrival) # Sorting processes according to arrival

    time = 0
    gantt =[]
    turnaround = []
    waiting = []

    for i in l:
        time+=i.burst
        turnaround.append(time-i.arrival) 
        if turnaround[-1]-i.burst<0:
            waiting.append(0)
        else:
            waiting.append(turnaround[-1]-i.burst)
        gantt+=[i.index for j in range(i.burst)]

    print("FCFS: ")
    print(gantt)
    print()
    
    return sum(turnaround)/len(turnaround), sum(waiting)/len(waiting)
#end fcfs


#start sjf non premptive
def sjf_np(l, interval):
    l = sorted(l, key=lambda process: process.burst) # Sorting processes according to burst time

    t = 0
    time = []
    k = -1

    while True:
        k+=1
        k%=len(l)

        if l[k].arrival <= t and l[k].t2 >=1:
            current = l[k]
        else:
            continue

        for _ in range(current.t2):
            time.append(current.index)
            current.t2-=1
            t+=1

        chk = 0
        for i in l:
            if i.t2 !=0:
                chk += 1
                break
        if chk == 0:
            break
    print("SJF NP: ")
    print(time, "\n")

    turnaround = []
    waiting = []
    l = sorted(l, key=lambda process: process.index)

    for p in l:
        last = 0
        for k, j in enumerate(time, start=1):
            if j == p.index:
                last = k # Finding last time at which process p is active
        turnaround.append(last - p.arrival)
        waiting.append(turnaround[-1]-p.burst)
    return sum(turnaround)/len(turnaround), sum(waiting)/len(waiting)
#end sjf non premptive


#start sjf
def sjf(l, interval):
    l = sorted(l, key=lambda process: process.burst) # Sorting processes according to burst time

    time = []
    t=0 # Simulate time each loop is one second
    while(True):
        for i in l:
            if i.arrival<=t and i.t>=1: # if the process is arrived and not completed
                current = i
                break
            else:
                current = -1 # If all processes completed
        if current == -1:
            break
        time.append(current.index) # appending the process that is in process
        current.t-=1
        t+=1
    print("SJF: ")
    print(time, "\n")

    turnaround = []
    waiting = []
    l = sorted(l, key=lambda process: process.index)

    for p in l:
        last = 0
        k = 1 # keep track of position
        for j in time:
            if j == p.index:
                last = k # Finding last time at which process p is active
            k+=1
        turnaround.append(last - p.arrival)
        waiting.append(turnaround[-1]-p.burst)

    return sum(turnaround)/len(turnaround), sum(waiting)/len(waiting)
#end sjf

#start priority
def priority(l, interval):
    l = sorted(l, key=lambda process: process.priority)

    t = 0
    time = []

    while(True):
        for i in l:
            if i.arrival <= t and i.complete == False:
                current = i  # Selecting process arrived and not completed
                break
            else:
                current = -1
        if current == -1:
            break
        for i in range(current.burst):
            time.append(current.index)  # Finishing the process
            t += 1
        current.complete = True
    print("PRIORITY: ")
    print(time, "\n")

    turnaround = []
    waiting = []
    l = sorted(l, key=lambda process: process.index)

    for p in l:
        last = 0
        k = 1  # keep track of position
        for j in time:
            if j == p.index:
                last = k  # Finding last time at which process p is active
            k += 1
        turnaround.append(last - p.arrival)
        waiting.append(turnaround[-1]-p.burst)

    return sum(turnaround)/len(turnaround), sum(waiting)/len(waiting)
#end priority

#round robins
def round_robins(l, interval):
    l = sorted(l, key=lambda process: process.index) # Sorting processes according to burst time

    t = 0
    time = []
    k = -1

    while True:
        k+=1
        k%=len(l)

        if l[k].arrival <= t and l[k].t1 >=1:
            current = l[k]
        else:
            continue

        if current.t1 >= interval:
            for _ in range(interval):
                time.append(current.index)
                current.t1 -= 1
                t += 1
        else:
            for _ in range(current.t1):
                time.append(current.index)
                t+=1
            current.t1 = 0
        chk = 0
        for i in l:
            if i.t1 !=0:
                chk += 1
                break
        if chk == 0:
            break
    print("ROUND ROBINS: ")
    print(time, "\n")

    turnaround = []
    waiting = []
    l = sorted(l, key=lambda process: process.index)

    for p in l:
        last = 0
        for k, j in enumerate(time, start=1):
            if j == p.index:
                last = k # Finding last time at which process p is active
        turnaround.append(last - p.arrival)
        waiting.append(turnaround[-1]-p.burst)
    return sum(turnaround)/len(turnaround), sum(waiting)/len(waiting)
#end round robins


if __name__ == '__main__':
    algorithms = [fcfs, sjf, sjf_np, priority, round_robins] # list of functions


    n = int(input("Enter the number of processes \n"))
    l = []  # List of processes

    for i in range(n):
        print("For process", i+1,
            "enter index, arrival, burst time and priority\n(Space seperated)")
        ind, a, b, pri = map(int, input().strip().split())
        print()
        p = Process(ind, a, b, pri)
        l.append(p)

    interval = int(input('Enter interval for round robins algorithm: '))
    print()

    turnaround_times =[] #average waiting times of all algorithms
    waiting_times =[]

    for i in algorithms:
        t, w = i(l, interval)
        turnaround_times.append(round(t,2))
        waiting_times.append(round(w,2))

    df = pd.DataFrame(np.array([["FCFS", "SJF", "SJF NP","Priority","Round Robins"], turnaround_times, waiting_times]).transpose(), columns=['Algorithms', 'Avg Turnaround Time','Avg Waiting Time'])
    print(df)


# OUTPUT 01
# PS C:\Users\HP\Rupesh\PICT\TE SEM 1\LP1\SPOS Lab\Assignment 01> python -u "c:\Users\HP\Rupesh\PICT\TE SEM 1\LP1\SPOS Lab\Assignment 01\Assignment01.py"
# Enter the number of processes 
# 4
# For process 1 enter index, arrival, burst time and priority
# (Space seperated)
# 1 5 4 6

# For process 2 enter index, arrival, burst time and priority
# (Space seperated)
# 2 3 5 2

# For process 3 enter index, arrival, burst time and priority
# (Space seperated)
# 3 0 7 1

# For process 4 enter index, arrival, burst time and priority
# (Space seperated)
# 4 4 4 4

# Enter interval for round robins algorithm: 3

# FCFS:
# [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 4, 4, 4, 4, 1, 1, 1, 1]

# SJF:
# [3, 3, 3, 2, 4, 1, 1, 1, 1, 4, 4, 4, 2, 2, 2, 2, 3, 3, 3, 3]

# SJF NP:
# [3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 2, 2, 2, 2, 2]

# PRIORITY:
# [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 4, 4, 4, 4, 1, 1, 1, 1]

# ROUND ROBINS:
# [3, 3, 3, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1, 1, 1, 2, 2, 3, 4, 1]

#      Algorithms Avg Turnaround Time Avg Waiting Time
# 0          FCFS               10.75             5.75
# 1           SJF               11.25             6.25
# 2        SJF NP               10.25             5.25
# 3      Priority               10.75             5.75
# 4  Round Robins                15.5             10.5

# OUTPUT 02
# PS C:\Users\HP\Rupesh\PICT\TE SEM 1\LP1\SPOS Lab\Assignment 01> python -u "c:\Users\HP\Rupesh\PICT\TE SEM 1\LP1\SPOS Lab\Assignment 01\Assignment01.py"
# Enter the number of processes 
# 3       
# For process 1 enter index, arrival, burst time and priority
# (Space seperated)
# 1 3 4 5

# For process 2 enter index, arrival, burst time and priority
# (Space seperated)
# 2 0 7 3

# For process 3 enter index, arrival, burst time and priority
# (Space seperated)
# 3 2 4 2

# Enter interval for round robins algorithm: 3

# FCFS:
# [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1]

# SJF:
# [2, 2, 3, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2, 2]

# SJF NP:
# [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3]

# PRIORITY:
# [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1]

# ROUND ROBINS:
# [2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 1, 2]

#      Algorithms Avg Turnaround Time Avg Waiting Time
# 0          FCFS                9.33             4.33
# 1           SJF                 9.0              4.0
# 2        SJF NP                9.33             4.33
# 3      Priority                9.33             4.33
# 4  Round Robins               12.33             7.33

# OUTPUT 03
# Enter the number of processes 
# 2
# For process 1 enter index, arrival, burst time and priority
# (Space seperated)
# 1 0 3 2

# For process 2 enter index, arrival, burst time and priority
# (Space seperated)
# 2 1 4 1

# Enter interval for round robins algorithm: 2

# FCFS:
# [1, 1, 1, 2, 2, 2, 2]

# SJF:
# [1, 1, 1, 2, 2, 2, 2]

# SJF NP:
# [1, 1, 1, 2, 2, 2, 2]

# PRIORITY:
# [1, 1, 1, 2, 2, 2, 2]

# ROUND ROBINS:
# [1, 1, 2, 2, 1, 2, 2]

#      Algorithms Avg Turnaround Time Avg Waiting Time
# 0          FCFS                 4.5              1.0
# 1           SJF                 4.5              1.0
# 2        SJF NP                 4.5              1.0
# 3      Priority                 4.5              1.0
# 4  Round Robins                 5.5              2.0
# PS C:\Users\HP\Rupesh\PICT\TE SEM 1\LP1\SPOS Lab\Assignment 01>