# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:21:30 2022

@author: Edward Flagg

https://realpython.com/python-gui-tkinter
Tutorial: Python GUI Programming With Tkinter
"""

import tkinter as tk

window = tk.Tk()


greeting = tk.Label(
    text="Python fucking sucks",
    fg = "white",
    bg = "black",
    width = 20,
    height = 10)
greeting.pack()

"""
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
"""

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

name = entry.get()
print(name)


window.mainloop()