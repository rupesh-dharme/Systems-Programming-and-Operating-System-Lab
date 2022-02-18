# Name: Rupesh Dharme
# Class: TE 01
# Batch: K1
# Roll no: 31124

# Problem statement:
#   Implementation of CPU Scheduling Algorithms: FCFS , SJF (Preemptive),
#   Priority (NonPreemptive) and Round Robin (Preemptive)

class Process():
    def __init__(self, index, arrival, burst, priority):
        self.index = index
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.complete = False  # to mark a process completed

    def show(self):
        print("Process", self.index, "details:")
        print("Priority", self.priority)
        print("Arrival time (in seconds)", self.arrival)
        print("Burst time (in seconds)", self.burst)
        print()


n = int(input("Enter the number of processes \n"))
l = []  # List of processes

for i in range(n):
    print("For process", i+1,
          "enter index, arrival, burst time and priority\n(Space seperated)")
    ind, a, b, pri = map(int, input().strip().split())
    print()
    p = Process(ind, a, b, pri)
    l.append(p)

# Sorting processes according to priority
l = sorted(l, key=lambda process: process.priority)

for i in l:
    i.show()

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

print("Priority algorithm Stats:")
print("Turnaround times:", turnaround)
print("Waiting times:", waiting)
print("Average turnaround times:", sum(turnaround)/n)
print("Average waiting times:", sum(waiting)/n)
print()
