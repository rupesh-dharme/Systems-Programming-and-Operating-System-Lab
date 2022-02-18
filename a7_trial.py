# Implementation of clock synchronization using Python programming language
# a. NTP
# b. Lamports clock

# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 07
from time import sleep

def processing():
    print('Recieving time from server', end='')
    for _ in range(3):
        sleep(1)
        print('.', end = '')
    print()

def ntp_clock_synchronization(t0):
    t0 = t0
    t1 = 1500
    t2 = 1502
    processing()
    t3 = int(input('What is time at your end now? '))
    offset = (abs(t1 - t0) + abs(t3 - t2))/2
    delay = ((t3 - t0) - (t2 - t1))/2
    sync_time = t2 + delay
    print(f'One way network delay is {delay}')
    print(f'Offset in network time and your time is {offset}')
    print(f'Synchronized time is {sync_time}')
    
if __name__ == '__main__':
    choice = int(input(open('prompt.txt', 'r').read()))
    match choice:
        case 1:
            time = int(input('What is time at your end? '))
            ntp_clock_synchronization(time)
        case _:
            print('Thank you')