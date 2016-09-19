import tkinter
import threading
from time import sleep
import network

color_i = 0
drawed_c, drawed_s = [], []
colors = ["white", "black", "red", "green", "blue", "yellow"]
def draw(canvas, circles, squares):
    for i in range(len(circles)):
        x, y, r = circles[i]
        if (len(drawed_c) > i):
            canvas.coords(drawed_c[i], x - r, y - r, x + r, y + r)
            canvas.itemconfig(drawed_c[i], fill=colors[color_i])
        else:
            drawed_c.append(canvas.create_oval(x - r, y - r, x + r, y + r, fill=colors[color_i]))
    for i in range(len(circles), len(drawed_c)):
        canvas.coords(drawed_c[i], -1, -1, -1, -1)
        
    """
    for i in range(len(squares)):
        x, y, r = squares[i]
        if (len(drawed_s) > i):
            canvas.coords(drawed_s[i], x - r, y - r, x + r, y + r)
        else:
            drawed_s.append(canvas.create_rectangle(x - r, y - r, x + r, y + r))
    """

    canvas.pack()


def idle_func():
    global color_i
    color_i += 1
    color_i %= 5
    circles, squares = network.get_objs()
    draw(canvas, circles, squares)
    canvas.after(20, idle_func)

network.init_net()
tk = tkinter.Tk()
canvas = tkinter.Canvas(tk)

canvas.pack()
idle_func()
tk.mainloop()
print(1)


