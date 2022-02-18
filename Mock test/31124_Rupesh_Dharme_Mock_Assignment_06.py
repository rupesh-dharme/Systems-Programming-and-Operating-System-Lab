class Memory_management:
    def __init__(self, _blocks, _processes) -> None:
        self.blocks = _blocks
        self.processes = _processes
    
    def first(self):
        summary = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            for block in blocks:
                if process[0] <= block:
                    i = blocks.index(block)
                    process.append(i+1)
                    blocks[i] -= process[0]
                    summary[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':block}
                    break
            if len(process) != 2:
                summary[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
                process.append('Waiting')
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in summary.keys():
            print(f'{i}'.ljust(9), f'{summary[i]["time"]}'.ljust(14), f'{summary[i]["block"]}'.ljust(12), f'{summary[i]["internal"]}'.ljust(15))

    def next(self):
        summary = {}
        blocks = self.blocks.copy()
        current = 0
        for process in self.processes:
            c = 0
            while True:
                if process[0] <= blocks[current]:
                    process.append(current)
                    blocks[current] -= process[0]
                    summary[self.processes.index(process)] = {'time': process[0], 'block': current+1, 'internal': blocks[current]}
                    break  
                current = (current + 1) % len(self.blocks)
                c += 1
                if c > len(blocks)-1: break
            if len(process) != 2:
                summary[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
                process.append('Waiting')
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in summary.keys():
            print(f'{i}'.ljust(9), f'{summary[i]["time"]}'.ljust(14), f'{summary[i]["block"]}'.ljust(12), f'{summary[i]["internal"]}'.ljust(15))

    def best(self):
        summary = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            try:
                block = min(i for i in blocks if i >= process[0])
            except:
                block = 'Waiting...'
            if block != 'Waiting...':
                i = blocks.index(block)
                blocks[i] -= process[0]
                summary[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':blocks[i]}
            else:
                summary[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in summary.keys():
            print(f'{i}'.ljust(9), f'{summary[i]["time"]}'.ljust(14), f'{summary[i]["block"]}'.ljust(12), f'{summary[i]["internal"]}'.ljust(15))

    def worst(self):
        summary = {}
        blocks = self.blocks.copy()
        for process in self.processes:
            try:
                block = max(i for i in blocks if i >= process[0])
            except:
                block = 'Waiting...'
            if block != 'Waiting...':
                i = blocks.index(block)
                blocks[i] -= process[0]
                summary[self.processes.index(process)] = {'time': process[0], 'block': i+1, 'internal':blocks[i]}
            else:
                summary[self.processes.index(process)] = {'time': process[0], 'block': 'Waiting...', 'internal': '-'}
        print('\nProcess'.ljust(9), 'Process time'.ljust(14), 'block'.ljust(12), 'fragmentation'.ljust(15))
        for i in summary.keys():
            print(f'{i}'.ljust(9), f'{summary[i]["time"]}'.ljust(14), f'{summary[i]["block"]}'.ljust(12), f'{summary[i]["internal"]}'.ljust(15))

if __name__ == '__main__':
    n = int(input("Enter number of blocks: "))
    m = int(input('Enter number of processes: '))
    blocks = [int(input(f'Block {i+1} size: ').strip()) for i in range(n)]
    processes = [[int(input(f'Process {i+1} size: ').strip())] for i in range(m)]
    memory = Memory_management(blocks, processes)
    prompt = "\nChoose the method of fitting you want to use: \n\t1. First fit \n\t2. Next fit \n\t3. Best fit \n\t4. Worst fit \n\t5. Exit\n"
    while True:
        choice = int(input(prompt))
        if choice == 1:
            memory.first()
        elif choice == 2:
            memory.next()
        elif choice == 3:
            memory.best()
        elif choice == 4:
            memory.worst()
        else:
            print('Thank you')
            break