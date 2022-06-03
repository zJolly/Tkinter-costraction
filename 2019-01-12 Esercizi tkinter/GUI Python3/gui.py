#!/usr/bin/python3

from tkinter import *

FinestraPrincipale = Tk()
# I componeti vanno inseriti tra la finestra e il loop

# Dimensione GUI
FinestraPrincipale.geometry("640x480+50+50")
# Nome GUI
FinestraPrincipale.title("GUI PYTHON 3")

# Il .pack serve per agganciare i widget alla GUI


etichetta = Label(FinestraPrincipale, text= "Questa è un'etichetta!")
etichetta.pack()

# Modifica colorazione etichetta
etichetta["fg"] = "red"
etichetta["bg"] = "#00ff55"
etichetta["pady"] = 5

premi = Button(FinestraPrincipale)
premi.pack()

# Modifica dimensioni del bottone e posizionamento nella GUI
premi["text"] = "Clicca qui!"
premi["height"] = 5
premi["width"] = 60
premi["pady"] = 5

scrivi = Entry(FinestraPrincipale, width = 30, bg = "black", fg = "green")
scrivi.pack()

pannello = Frame(FinestraPrincipale)
pannello.pack()
b1 = Button(pannello, text ="Bottone 1")
b2 = Button(pannello, text ="Bottone 2")
b1.pack(side = LEFT)
b2.pack(side = RIGHT)


# Mette in loop la finestra... e aspetta un evento!
FinestraPrincipale.mainloop()
