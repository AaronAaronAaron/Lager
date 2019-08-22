import tkinter as tk
from tkinter import ttk
#Tk/TTk config
root = tk.Tk()
canvasheight, canvaswidth = 800, 800
root.geometry(str(canvaswidth)+"x"+str(canvasheight))
root.title("TK Mandelbrot")
w = tk.Canvas(root, width=canvaswidth, height=canvasheight)
e1=ttk.Entry(root)
style=ttk.Style()
style.configure("TButton", font=("Helvetica", 30, "bold"))




def main():
    startmandelttk.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



def _rgb(rgb):
    return "#%02x%02x%02x" % rgb


def mandel(c):
    maxiter=50
    z = 0
    i = 0
    for h in range(0, maxiter):
        z = z * z + c
        if abs(z) > 2:
            break
        else:
            i += 1
    if abs(z) >= 2:
        return 5*i

    else:
        return 0


def Mandelbrot():
    startmandelttk.destroy()
    w.pack()
    for x in range(0, canvaswidth):
        real = x / (canvaswidth/3) - 2.2
        for y in range(0, canvasheight):
            imag = y / (canvasheight/3) - 1.5
            c = complex(real, imag)
            p = mandel(c)
            w.create_line(x, canvasheight - y, x + 1, canvasheight + 1 - y, fill=_rgb((p, 0, 0)))
            w.pack()


startmandelttk = ttk.Button(root, text="Start", command=Mandelbrot, style="TButton")
main()
root.mainloop()