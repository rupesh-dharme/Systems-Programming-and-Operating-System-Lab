# Name: Rupesh Dharme
# Class: TE 01
# Batch: K1
# Roll no: 31124

# Problem statement: 
#   Implementation of CPU Scheduling Algorithms: FCFS , SJF (Preemptive), 
#   Priority (Non-Preemptive) and Round Robin (Preemptive)

class Process():
    def __init__(self,index, arrival, burst):
        self.index = index
        self.arrival = arrival
        self.burst = burst

    def show(self):
        print("Process",self.index,"details:")
        print("Arrival time (in seconds)",self.arrival)
        print("Burst time (in seconds)",self.burst)
        print()

n = int(input("Enter the number of processes \n"))
l = []
for i in range(n):
    print("For process",i+1,"enter index, arrival and burst time\n(Space seperated)")
    ind, a, b = map(int, input().strip().split())
    print()
    p = Process(ind, a, b)
    l.append(p)

l = sorted(l, key=lambda process: process.arrival) # Sorting processes according to arrival
for i in l:
    i.show()

time = 0
turnaround = []
waiting = []

for i in l:
    time+=i.burst
    turnaround.append(time-i.arrival) 
    if turnaround[-1]-i.burst<0:
        waiting.append(0)
    else:
        waiting.append(turnaround[-1]-i.burst)

print("FCFS Stats:")
print("Turnaround times:",turnaround)
print("Waiting times:",waiting)
print("Average turnaround times:",sum(turnaround)/n)
print("Average waiting times:",sum(waiting)/n)
print()