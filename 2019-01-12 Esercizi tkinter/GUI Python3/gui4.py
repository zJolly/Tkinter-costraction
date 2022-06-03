#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox

def stampa1():
    messagebox.showinfo('Messaggio', 'Dentro stampa 1')

def stampa2(messaggio):
    messagebox.showinfo('Messaggio', messaggio)

def stampa3(haiPremuto):
    messaggio = haiPremuto.widget['text']
    messagebox.showinfo('Alunno: ', messaggio )
    # implementeremo il codice successivamente


window = Tk()

window.geometry("640x480+350+350")
window.title("GUI 4.0 PYTHON 3")
pannello = Frame(window)
# expand  e fill servono per rendere il Frame grande come tutta la finestara
pannello.pack(expan = True, fill = BOTH)
pannello['background'] = 'pink'

b0 = Button(pannello, text = 'B0', command = stampa1)
b1 = Button(pannello, text = 'B1', command = lambda: stampa2('Premuto B1'))
b2 = Button(pannello, text = 'B2', command = lambda: stampa2('Premuto B2'))

b0.place(relx = 0.15, rely = 0.15, anchor = CENTER)
b1.place(x = 100, y = 140, anchor = CENTER)
b2.place(x = 100, y = 180, anchor = CENTER)

alunni = ['Buzzi', 'Cimenti', 'Zoratto', 'Pascolo', 'Soprano']
x1 = 100
for singolo in alunni:
    # Non funzione l'ascoltatore!
    #bottone = Button(pannello, text = singolo, command = lambda: stampa2(singolo))
    bottone = Button(pannello, text = singolo)
    bottone.bind('<ButtonRelease-1>', stampa3)
    bottone.place(x = x1 , y = 200 , width = 100)
    x1 = x1 + 100




window.mainloop()
