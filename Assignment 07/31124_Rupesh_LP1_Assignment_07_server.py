# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 07

import socket,datetime,time,random

host=None
port=None
s=None
def create_socket():
    global host
    global port
    global s
    host=""
    port=9999
    try:
        s=socket.socket()
    except socket.error as e:
        print("Socket creation error: ",e)

def bind_socket():
    global host
    global port
    global s
    try:
        print("Binding the port:",port)
        s.bind((host,port))
        print("Listening...")
        s.listen(5)
    except socket.error as e:
        print("Binding error: ",e,"\nRetrying...")
        bind_socket()

def socket_accept():
    global host
    global port
    global s
    try:
        connection,address=s.accept()
        print(f"connection: {connection}\naddress: {address}")
        send_commands(connection)
        if connection:
            connection.close()
    except socket.error as e:
        print("Socket accept error: ",e,"\nRetrying...")

def send_commands(connection):
    d=datetime.datetime
    while True:
        response = str(connection.recv(1024), "utf-8")
        time.sleep(0.857*random.randint(5,10))
        t1=int(d.now().timestamp())
        if response=="q":
            return
        if response=="lamport":
            time.sleep(1 * random.randint(0, 5))
            connection.send(str.encode(f"timestamp {int(d.now().timestamp())}"))
        if response=="ntp":
            time.sleep(1 * random.randint(0, 5))
            connection.send(str.encode(f"{t1} {int(d.now().timestamp())}"))

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()