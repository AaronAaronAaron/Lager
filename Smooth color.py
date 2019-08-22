import tkinter as tk
from tkinter import ttk
import math as m
import colorsys
#Tk/TTk config
root = tk.Tk()
canvasheight, canvaswidth = 800, 800
root.geometry(str(canvaswidth)+"x"+str(canvasheight))
root.title("TK Mandelbrot")
w = tk.Canvas(root, width=canvaswidth, height=canvasheight)
e1=ttk.Entry(root)
style=ttk.Style()
style.configure("TButton", font=("Helvetica", 30, "bold"))
maxiter=80


def main():
    startmandelttk.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def mandel(c):
    z = 0
    i = 0
    while abs(z)<= 2 and i < maxiter:
        z = z * z + c
        i += 1
    if i== maxiter:
        return maxiter
    return i + 1 - m.log(m.log2(abs(z)))


def Mandelbrot():
    global p
    startmandelttk.destroy()
    w.pack()
    for x in range(0, canvaswidth):
        real = x / (canvaswidth/3) - 2.2
        for y in range(0, canvasheight):
            imag = y / (canvasheight/3) - 1.5
            c = complex(real, imag)
            p = mandel(c)
            w.create_line(x, canvasheight - y, x + 1, canvasheight + 1 - y, fill="#" + hsvtorgbtohexa())
            w.pack()
def hsvtorgbtohexa():
    hue=int(255 * p/maxiter)
    saturation= 1
    value= 255 if p < maxiter else 0
    rgbtuple=colorsys.hsv_to_rgb(hue,saturation,value)
    print(rgbtuple)
    r=hex(int(rgbtuple[0]))[2:]
    g=hex(int(rgbtuple[1]))[2:]
    b=hex(int(rgbtuple[2]))[2:]
    if len(r) < 2:
        r = "0" + r
    if len(g) < 2:
        g = "0" + g
    if len(b) < 2:
        b = "0" + b
    print(r+g+b)
    return r+g+b
startmandelttk = ttk.Button(root, text="Start", command=Mandelbrot, style="TButton")
main()
root.mainloop()