from tkinter import *
import tkinter.messagebox
from time import strftime
tk = Tk()
tk.title('Clock')
label = Label(tk, font = ('ds-digital',80),background='cyan',foreground='black')
label.pack(anchor='center')
def fetchtime():
    t = strftime('%H : %M : %S %p')
    label.config(text=t)
    label.after(1000,fetchtime)
fetchtime()
tk.mainloop()