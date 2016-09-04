import tkinter
import threading
from time import sleep
import network

i = 0
drawed = []
def draw(cvs, arr):
    for i in range(len(arr)):
        x, y, r = arr[i]
        if (len(drawed) > i):
            cvs.coords(drawed[i], x - r, y - r, x + r, y + r)
        else:
            drawed.append(cvs.create_oval(x - r, y - r, x + r, y + r))
    cvs.pack()


def idle_func(arg):
    arr = network.get_objs()
    draw(cvs, arr)

def idle_th_func():
    while True:
        tk.event_generate("<<idle-event>>")
        sleep(0.02)

network.init_net()
tk = tkinter.Tk()
cvs = tkinter.Canvas(tk)
circle = cvs.create_oval(10, 10, 20, 20)

idle_thread = threading.Thread(target=idle_th_func)
idle_thread.start()
cvs.pack()
tk.bind("<<idle-event>>", idle_func)
tk.mainloop()
print(1)


