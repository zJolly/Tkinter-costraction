#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

litri=0
prezzo=0
tot=0

def risultato():
    global litri, prezzo
    tot= prezzo * litri
    scrivi3['text'] = tot

finestrone = Tk()

finestrone.geometry("500x50+550+550")
finestrone.title("Distributore D'Aronco")

pannello = Frame(finestrone)
pannello.pack()

etichetta1 = Label(pannello, text= "Litri erogati:")
etichetta1.pack(side = LEFT)
scrivi1 = Entry(pannello, bg = "green", fg = "black", textvariable = litri)
scrivi1.pack(side = RIGHT)
etichetta2 = Label(pannello, text= "Prezzo al litro:")
etichetta2.pack(side = RIGHT)
scrivi2 = Entry(pannello, bg = "green", fg = "black", textvariable = prezzo)
scrivi2.pack(side = RIGHT)

pannello1 = Frame(finestrone)
pannello1.pack()
b1 = Button(pannello1, text ="Calcolo totale", command = risultato)
b1.pack(side = LEFT)
etichetta3 = Label(pannello1, text= "Paga alla cassa:")
etichetta3.pack(side = LEFT)
scrivi3 = Entry(pannello1)
scrivi3.pack(side = RIGHT)

prezzo = DoubleVar()
litri = DoubleVar()

finestrone.mainloop()
