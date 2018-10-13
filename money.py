from tkinter import *
from random import randint
import time 
main = Tk()
c = Canvas(main, width=600, height=600)
c.pack()
money = randint(100, 600)
c.create_rectangle(200, 150, 400, 350, fill="white")
c.create_rectangle(180, 130, 420, 180, fill="white")
def Get_Money(event):
    for i in range(10):
        c.move(2, 0, -7)
        main.update()
        time.sleep(0.01)
    a = 0
    b = int(money/8)
    for i in range(b):
        c.create_rectangle(275, 590-a, 325, 570-a, fill="green")
        a += 2
    c.create_text(300, 400, text="You got %s money" % money, font=(
    'Helvetica', 30))
c.bind_all("<KeyPress-space>", Get_Money)

