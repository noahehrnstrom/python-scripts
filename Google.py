from tkinter import *
from time import sleep
from random import randint

tk = Tk()
c = Canvas(tk, width=1000, height=800)
tk.wm_attributes("-topmost", 1)
c.pack()

a = 1

while True:
 
 rand = randint(1, 4)
 
 if rand == 1:
  c.create_text(500, 800, text="Google", font=("Courier", 200), fill="red")
 elif rand == 2:
  c.create_text(500, 800, text="Google", font=("Courier", 200), fill="blue")
 elif rand == 3:
  c.create_text(500, 800, text="Google", font=("Courier", 200), fill="orange")
 else:
  c.create_text(500, 800, text="Google", font=("Courier", 200), fill="green")
 for i in range(100):
  c.move(a, 0, -9.6)
  sleep(0.01)
  tk.update()
 a = a + 1
