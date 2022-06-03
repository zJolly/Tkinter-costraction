#!/usr/bin/python3

from tkinter import *

finestrone = Tk()

finestrone.geometry("480x100+550+550")
finestrone.title("Pannello connessione")

pannello = Frame(finestrone)
pannello.pack()

etichetta1 = Label(pannello, text= "Per vedere delle belle cose devi... essere conesso")
etichetta1.grid(row = 0, column = 1)
etichetta3 = Label(pannello, text = "Indirizzo IP:")
etichetta3.grid(row = 1, column = 1)
scrivi1 = Entry(pannello)
scrivi1.grid(row = 1, column = 2)
etichetta4 = Label(pannello, text = "Porta:")
etichetta4.grid(row = 1, column = 3)
scrivi3 = Entry(pannello)
scrivi3.grid(row = 1, column = 4)
etichetta2 = Label(pannello, text= "username:")
etichetta2.grid(row = 2, column = 1)
scrivi2 = Entry(pannello)
scrivi2.grid(row = 2, column = 2)




finestrone.mainloop()
