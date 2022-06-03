#!/usr/bin/python3

from tkinter import *

Finestrella = Tk()

Finestrella.geometry("200x250+100+150")

etichetta = Label(Finestrella, text= "Somma A+B")
etichetta.pack()
etichetta1 = Label(Finestrella, text= "Inserisci primo numero:")
etichetta1.pack()

spazio = Entry(Finestrella, width = 30, bg = "grey")
spazio.pack()
etichetta2 = Label(Finestrella, text= "Inserisci secondo numero:")
etichetta2.pack()
spazia = Entry(Finestrella, width = 30, bg = "grey")
spazia.pack()

pannello = Frame(Finestrella)
pannello.pack()
b1 = Button(pannello, text ="+")
b2 = Button(pannello, text ="-")

b1.pack(side = LEFT)
b2.pack(side = RIGHT)
pannello1 = Frame(Finestrella)
pannello1.pack()
b3 = Button(pannello, text ="*")
b4 = Button(pannello, text ="/")
b3.pack(side = LEFT)
b4.pack(side = RIGHT)

Finestrella.mainloop()
