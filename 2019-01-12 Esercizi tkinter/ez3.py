#!/usr/bin/python3

from tkinter import *

finestrone = Tk()

finestrone.geometry("480x100+550+550")

pannello = Frame(finestrone)
pannello.pack()

etichetta1 = Label(pannello, text= "Username:")
etichetta1.grid(row = 0, column = 1)
scrivi1 = Entry(pannello)
scrivi1.grid(row = 0, column = 3)
etichetta2 = Label(pannello, text= "Password:")
etichetta2.grid(row = 2, column = 1)
scrivi2 = Entry(pannello)
scrivi2.grid(row = 2, column = 3)

pannello1 = Frame(finestrone)
pannello1.pack()

b1 = Button(pannello1, text ="Accedi")
b2 = Button(pannello1, text ="Annulla")
b1.pack(side = LEFT)
b2.pack(side = RIGHT)



finestrone.mainloop()
