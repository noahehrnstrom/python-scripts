# python-scripts
python scripts
I'm working in python with function module tkinter
to make fun and simple games.
This is how you open a tk-window with tkinter:

from tkinter import *

main = Tk()
main.resizable(0, 0)
main.wm_attributes("-topmost", 1)
c = Canvas(main, width=600, height=600, bd=0, highlightthickness=0)
c.pack()
main.update()

That was it!
