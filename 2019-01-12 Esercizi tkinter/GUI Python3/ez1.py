#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

Finestrella = Tk()

Finestrella.geometry("300x150+100+150")
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
b1 = Button(pannello, text ="Bottone 1")
b1.pack()

Finestrella.mainloop()
