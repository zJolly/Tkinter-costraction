#!/usr/bin/python3

from tkinter import *

finestrone = Tk()

finestrone.geometry("600x50+550+550")

pannello = Frame(finestrone)
pannello.pack()

etichetta1 = Label(pannello, text= "Numero decimale:")
etichetta1.pack(side = LEFT)
scrivi1 = Entry(pannello)
scrivi1.pack(side = RIGHT)
etichetta2 = Label(pannello, text= "Numero convertito:")
etichetta2.pack(side = RIGHT)
scrivi2 = Entry(pannello, bg = "green", fg = "black")
scrivi2.pack(side = RIGHT)

pannello1 = Frame(finestrone)
pannello1.pack()

etichetta3 = Label(pannello1, text= "Convertitore in base:")
etichetta3.pack(side = LEFT)
rb1 = Radiobutton(pannello1, text = "Due", value = "okk")
rb2 = Radiobutton(pannello1, text = "Otto", value = "kko")
rb3 = Radiobutton(pannello1, text = "Sedici", value = "oko")
rb1.pack(side = LEFT)
rb2.pack(side = LEFT)
rb3.pack(side = LEFT)
premi = Button(pannello1, text = 'Converti')
premi.pack(side = RIGHT)

finestrone.mainloop()
