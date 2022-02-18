# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 06

# Problem Statement: Write a program in C++/Java/Python to simulate 
#                    memory placement strategies- First fit, next fit, Best fit and Worst fit

class Memory_management:
    def __init__(self, _blocks, _processes) -> None:
        self.blocks = _blocks
        self.processes = _processes
    
    def first_fit(self):
        table = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            for block in blocks:
                if process[0] <= block:
                    i = blocks.index(block)
                    process.append(i+1)
                    blocks[i] -= process[0]
                    table[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':block}
                    break
            if len(process) != 2:
                table[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
                process.append('Waiting')
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in table.keys():
            print(f'{i}'.ljust(9), f'{table[i]["time"]}'.ljust(14), f'{table[i]["block"]}'.ljust(12), f'{table[i]["internal"]}'.ljust(15))

    def next_fit(self):
        table = {}
        blocks = self.blocks.copy()
        ptr = 0
        for process in self.processes:
            c = 0
            while True:
                if process[0] <= blocks[ptr]:
                    process.append(ptr)
                    blocks[ptr] -= process[0]
                    table[self.processes.index(process)] = {'time': process[0], 'block': ptr+1, 'internal': blocks[ptr]}
                    break
                ptr = (ptr + 1) % len(self.blocks)  
                c += 1
                if c > len(blocks)-1: break
            if len(process) != 2:
                table[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
                process.append('Waiting')
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in table.keys():
            print(f'{i}'.ljust(9), f'{table[i]["time"]}'.ljust(14), f'{table[i]["block"]}'.ljust(12), f'{table[i]["internal"]}'.ljust(15))

    def best_fit(self):
        table = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            try:
                block = min(i for i in blocks if i >= process[0])
            except:
                block = 'Waiting...'
            if block != 'Waiting...':
                i = blocks.index(block)
                blocks[i] -= process[0]
                table[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':blocks[i]}
            else:
                table[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in table.keys():
            print(f'{i}'.ljust(9), f'{table[i]["time"]}'.ljust(14), f'{table[i]["block"]}'.ljust(12), f'{table[i]["internal"]}'.ljust(15))

    def worst_fit(self):
        table = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            try:
                block = max(i for i in blocks if i >= process[0])
            except:
                block = 'Waiting...'
            if block != 'Waiting...':
                i = blocks.index(block)
                blocks[i] -= process[0]
                table[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':blocks[i]}
            else:
                table[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in table.keys():
            print(f'{i}'.ljust(9), f'{table[i]["time"]}'.ljust(14), f'{table[i]["block"]}'.ljust(12), f'{table[i]["internal"]}'.ljust(15))

if __name__ == '__main__':
    n = int(input("Enter number of blocks: "))
    m = int(input('Enter number of processes: '))
    blocks = [int(input(f'Block {i+1} size: ').strip()) for i in range(n)]
    processes = [[int(input(f'Process {i+1} size: ').strip())] for i in range(m)]
    memory = Memory_management(blocks, processes)
    with open('Assignment 06\prompt.txt', 'r') as f:
        prompt = f.read()
    while True:
        choice = int(input(prompt))
        if choice == 1:
            memory.first_fit()
        elif choice == 2:
            memory.next_fit()
        elif choice == 3:
            memory.best_fit()
        elif choice == 4:
            memory.worst_fit()
        else:
            print('Thank you')
            break

        # match choice:
        #     case 1:
        #         memory.first_fit()
        #     case 2:
        #         memory.next_fit()
        #     case 3:
        #         memory.best_fit()
        #     case 4:
        #         memory.worst_fit()
        #     case _:
        #         print('Thank you')
        #         break