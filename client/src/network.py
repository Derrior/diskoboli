import socket
import os
from sys import byteorder as BO
from time import time, sleep
import threading
from select import select

ObjectsQuery = 1


def get_data(sock, length, timeout):
    ready = select([sock], [], [], timeout)
    if (ready[0]):
        data = sock.recv(length)
    else:
        exit()
    return data

ip = "127.0.0.1"
Port = 5051
data = bytearray(1024 * 1024)

sock = None

def init_net():
    global sock
    sock = socket.socket()
    sock.connect((ip, Port))
    d = get_data(sock, 2, 1)
    print(d)


def byte2num(arr, i):
    return int.from_bytes(arr[i:i + 4], BO)

def parse(arr, Type):
    ret = []
    if (Type == ObjectsQuery):
        ret = [0] * byte2num(arr, 0)
        idx = 4
        for i in range(len(ret)):
            ret[i] = [byte2num(arr, idx), byte2num(arr, idx + 4), byte2num(arr, idx + 8)]
            idx += 12
    return ret

def get_objs():
    data[0] = ObjectsQuery
    sock.send(data[:1])
    ans = get_data(sock, 1024 * 1024, 1)
    return parse(ans, ObjectsQuery)

