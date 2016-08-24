import os
import time
import socket
import threading
import sys
from select import select

clients = []



Port = 7179
ANS = bytearray(1)
ANS[0] = 1
InitQuery     = 0
ObjectsQuery  = 1
KeyboardQuery = 2
PingQuery     = 3
ExitQuery     = 4

clients_amount_max = 8
client_colors = ['yellow', 'blue', 'green', 'red', 'brown', 'cyan', 'magenta']
unused_colors = [0] * 7

def get_data(client, length, timeout):
    ready = select([client], [], [], timeout)
    if (ready):
        data = client.recv(length)
        return data
    else:
        return None
    

run_thread = 0
sock = 0

time_begin = time.time()

def thread_f():
    global run_thread, sock, client_num
    run_thread = 1
    for i in range(100000):
        try:
            conn, addr = sock.accept()
        except Exception:
            return
        client_bytearray = bytearray(2)
        client_bytearray[0] = client_num
        conn.send(client_bytearray)
        client_num += 1
        j = 0
        color_num = 0
        while (client_colors[color_num]):
            color_num += 1
        client_colors[color_num] = 1
        clients.append([conn, addr, color_num, time.time()])
    Pretty("all connections got")
    run_thread = 0


exited = None

def quit_f():
    global exited 
    while True:
        
        input_str = input()
        if (input_str == 'q' or input_str == 'exit'):
            exited = True
        if (exited):
            break
    

def quick_ping(conn):
    conn.send(ANS)

def Pretty(*args):
    print(round(time.time() - time_begin, 3), *args)

quit_thread = threading.Thread(target=quit_f)

def init_net():
    global sock
    sock = socket.socket()
    
    sock.bind(("192.168.1.105", Port))
    sock.listen(8)
    thread = threading.Thread(target=thread_f)
    thread.start()
    quit_thread.start()

def update_net():
    print("UN begin")
    quit_thread.join(timeout=0.1)
    i = 0 
    while i < len(clients):
        if (time.time() - clients[i][-1] > 15):
            Pretty("client number %d disconnected" % i)
            client_colors[clients[i][2]] = 0
            clients.pop(i)
            continue
        conn = clients[i][0]
        data = get_data(conn, 1024, 0.1)
        if (not data):
            i += 1
            continue
        ask = data[0]
        Pretty(ask)
        quick_ping(conn)
        if 
        i += 1

    print("UN end")

def free_net():
    sock.close()

