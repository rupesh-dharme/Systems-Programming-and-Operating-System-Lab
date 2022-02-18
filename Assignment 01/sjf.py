# Name: Rupesh Dharme
# Class: TE 01
# Batch: K1
# Roll no: 31124

# Problem statement: 
#   Implementation of CPU Scheduling Algorithms: FCFS , SJF (Preemptive), 
#   Priority (NonPreemptive) and Round Robin (Preemptive)

class Process():
    def __init__(self,index, arrival, burst):
        self.index = index
        self.arrival = arrival
        self.burst = burst
        self.t = burst # to keep reduced time when partial process is done

    def show(self):
        print("Process",self.index,"details:")
        print("Arrival time (in seconds)",self.arrival)
        print("Burst time (in seconds)",self.burst)
        print()

n = int(input("Enter the number of processes \n"))
l = [] # List of processes

for i in range(n):
    print("For process",i+1,"enter index, arrival and burst time\n(Space seperated)")
    ind, a, b = map(int, input().strip().split())
    print()
    p = Process(ind, a, b)
    l.append(p)

l = sorted(l, key=lambda process: process.burst) # Sorting processes according to burst time

for i in l:
    i.show()

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

print("SJF Stats:")
print("Turnaround times:",turnaround)
print("Waiting times:",waiting)
print("Average turnaround times:",sum(turnaround)/n)
print("Average waiting times:",sum(waiting)/n)
print()