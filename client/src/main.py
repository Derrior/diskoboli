import tkinter
import threading
from time import sleep
import network

color_i = 0
drawed_c, drawed_s = [], []
colors = ["white", "black", "red", "green", "blue", "yellow"]
def draw(cvs, circles, squares):
    for i in range(len(circles)):
        x, y, r = circles[i]
        if (len(drawed_c) > i):
            cvs.coords(drawed_c[i], x - r, y - r, x + r, y + r)
            cvs.itemconfig(drawed_c[i], fill=colors[color_i])
        else:
            drawed_c.append(cvs.create_oval(x - r, y - r, x + r, y + r, fill=colors[color_i]))
    for i in range(len(circles), len(drawed_c)):
        cvs.coords(drawed_c[i], -1, -1, -1, -1)
        
    """
    for i in range(len(squares)):
        x, y, r = squares[i]
        if (len(drawed_s) > i):
            cvs.coords(drawed_s[i], x - r, y - r, x + r, y + r)
        else:
            drawed_s.append(cvs.create_rectangle(x - r, y - r, x + r, y + r))
    """


    cvs.pack()

def idle_thread_f():
    while True:
        tk.event_generate("<<idle-event>>")
        sleep(0.03)
    

def idle_func():
    global color_i
    color_i += 1
    color_i %= 5
    circles, squares = network.get_objs()
    draw(cvs, circles, squares)
    cvs.after(20, idle_func)

network.init_net()
tk = tkinter.Tk()
cvs = tkinter.Canvas(tk)
circle = cvs.create_oval(10, 10, 20, 20)

cvs.pack()
idle_func()
tk.mainloop()
print(1)


