# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 08

class Process:
    def __init__(self, _number, _status = 'active'):
        self.number = _number
        self.status = _status

def election_bully(processes, caller):
    processes.sort(key = lambda process : process.number)
    candidates = [caller]
    while True:
        l = []
        candidate = candidates.pop(0)
        for process in processes:
            if process.number > candidate.number and process.status == 'active':
                l.append(process)
        if not l:
            return candidate
        candidates = l

def election_ring(processes, caller):
    current = caller
    lst = []
    n = len(processes)
    c = processes.index(caller)
    while True:
        c += 1
        c = c%n
        if processes[c] is not caller:
            if processes[c].status == 'active':
                lst.append(processes[c])
        else:
            break
    lst.sort(key = lambda process : process.number)
    return lst[-1]

processes = []
while True:
    inp = input("Enter Process or 'quit': ")
    if inp == 'quit':
        print("Thank you")
        break
    num, status = inp.split()
    num = int(num)
    if status == 'a':
        processes.append(Process(num))
    else:
        processes.append(Process(num, 'inactive'))

print('Elected using Bully algorithm:', election_bully(processes, processes[1]).number)
print('Elected using Ring algorithm:', election_ring(processes, processes[1]).number)