#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *

window = Tk()

window.geometry("380x280+350+350")
window.title("GUI 2.0 PYTHON 3")

# CHECK BUTTON
scelta1 = Checkbutton(window, text = "Scelta 1")
scelta1.pack()
scelta2 = Checkbutton(window, text = "Scelta 2")
scelta2.pack()

pannello = Frame(window)
pannello.pack()

# RADIO BUTTON
rb1 = Radiobutton(pannello, text = "Promosso", value = "ok")
rb2 = Radiobutton(pannello, text = "Bocciato", value = "ko")
rb1.grid(row = 0, column = 0)
rb2.grid(row = 0, column = 1)

# AREA DI TESTO
testo = Text(pannello, width = 25, height = 5)
testo.grid(row = 1, columnspan = 2, padx = 5, pady = 5)

# SPINNER
spin = Spinbox(pannello, from_ = -10, to = 10)
spin.grid(row = 2, columnspan = 2)

# MENU DI SCELTA
menuplus = Menu(window)
menufile = Menu(menuplus, tearoff = 0)
menufile.add_command(label = 'Voce 1')
menufile.add_separator()
menufile.add_command(label = 'Voce 2')
menuplus.add_cascade(label = 'Menu 1', menu = menufile)


window.config(menu = menuplus)

# CASELLA COMBINATA DI SCELTA
elenco =Combobox(pannello)
elenco['values'] = ('Zoratto','Vidussi')
elenco.grid(row = 3, columnspan = 2, pady = 10)



window.mainloop()
