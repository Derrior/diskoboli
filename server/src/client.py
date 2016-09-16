import os
import time
import socket
import threading
from sys import byteorder as BO
from random import randint
from select import select

clients = []



Port = 5051
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

client_num = 0
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
        print("new_client")
        client_num += 1
        j = 0
        color_num = 0
        while (unused_colors[color_num]):
            color_num += 1
        client_colors[color_num] = 1
        clients.append([conn, addr, color_num, time.time()])
    Pretty("all connections got")
    run_thread = 0



def quick_ping(conn):
    conn.send(ANS)

def Pretty(*args):
    print(round(time.time() - time_begin, 3), *args)


def init_net():
    global sock
    sock = socket.socket()
    
    sock.bind(("127.0.0.1", Port))
    sock.listen(8)
    thread = threading.Thread(target=thread_f)
    thread.start()
    #quit_thread.start()

def num2byte(arr, i, n):
    arr[i:i + 4] = n.to_bytes(4, BO)

def to_bytes(arr):
    ret = bytearray(1024 * 1024)
    num2byte(ret, 0, len(arr))
    idx = 4
    for i in range(len(arr)):
        num2byte(ret, idx, arr[i][0])
        num2byte(ret, idx + 4, arr[i][1])
        num2byte(ret, idx + 8, arr[i][2])
        idx += 12
    return ret[:idx]


balls = [[randint(10, 100) for i in range(3)] for j in range(randint(5, 15))]

def update_net():
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
        clients[i][-1] = time.time()
        ask = data[0]
        Pretty(ask)
        if ask == ObjectsQuery:
            length = randint(2, len(balls))
            conn.send(to_bytes(balls[:length]))
            balls[0][0] += 2
        i += 1


def free_net():
    sock.shutdown(socket.SHUT_RDWR)
    print("hey")

