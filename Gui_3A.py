#!/usr/bin/python3

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

n=0

# Prototipo con popup
#def provaClick():textvariable = prezzo
    #messagebox.showinfo("Info","Il bottone funge!")
def incrementa():
    global n
    n=n+1
    # Convertitore da inero in stringa ------------------vvvvvv

    etichetta['text'] = "Il pulsante è stato premuto " + str(n) + " volte"

def decrementa():
    global n
    n=n-1
    etichetta['text'] = "Il pulsante è stato premuto " + str(n) + " volte"

def controllo():
    valore = valoreTesto.get() # mi ritorna il contenuto dell'Entry
    messagebox.showinfo("Info","Testo:" + valore)
    valoreTesto.set("")

    if(scelta1.state()):
        messagebox.showinfo("Info", "Check1 ON!")
    else:
        messagebox.showinfo("Info", "Check1 OFF!")



miaFinestra = Tk()
miaFinestra.title("Widget Tk")
miaFinestra.geometry("640x480+100+100")
contenitore = Frame(miaFinestra)
contenitore.pack()

# ETICHETTA
etichetta = Label(contenitore, text = "Premi i pulsanti: ")
etichetta.grid(row = 0, column = 0, columnspan = 2, padx = 5 , pady = 5 )
etichetta["font"] = ("Arial", 15)

# PULSANTE
pulsante1 = Button(contenitore, text = "Push -1", command = decrementa)
pulsante2 = Button(contenitore, text = "Push +1",command = incrementa)
pulsante1.grid(row = 1, column = 0, padx = 5 , pady = 5 )
pulsante2.grid(row = 1, column = 1, padx = 5 , pady = 5 )

# CASELLA DI TESTO
# IntVar()
# BooleanVar()
# DoubleVar()
valoreTesto = StringVar()
valoreTesto.set("Digita il testo qui dentro")
testo = Entry(contenitore, textvariable = valoreTesto)
testo.grid(row = 2, columnspan = 2, padx = 5 , pady = 5 )

# FOCUS SULL'OGGETTO
testo.focus()

# DISATTIVARE OGGETTO
#testo['state'] = "disabled"

# CHECK Button
v1 = BooleanVar()
v2 = BooleanVar()
v3 = BooleanVar()
v4 = BooleanVar()
scelta1 = Checkbutton(contenitore, text = "Scelta 1", textvariable = v1)
scelta1.grid(row = 3)
scelta2 = Checkbutton(contenitore, text = "Scelta 2", textvariable = v2)
scelta2.grid(row = 3, column = 1, padx = 5 , pady = 5 )


# RADIO BUTTON (pulsanti di scelta)
radio1 = Radiobutton(contenitore, text = "Alto", value = "a", textvariable = v3)
radio2 = Radiobutton(contenitore, text = "Basso", value = "b", textvariable = v3)
radio1.grid(row = 4, column = 0)
radio2.grid(row = 4, column = 1, padx = 5 , pady = 5 )


# TEXT AREA
testo = Text(contenitore, height=5, width=25)
testo.grid(row = 5, columnspan = 2, padx = 5, pady = 5)

# SPINNER
spin = Spinbox(contenitore, from_= 0, to = 100)
spin.grid(row = 6, columnspan = 2, padx = 5, pady = 5)
var =IntVar()
var.set(50)
spin['textvariable'] = var

# CASELLA COMBINATA (COMBOBOX)
# aggiungere --> from tkinter.ttk import *
combo = Combobox(contenitore)
# Imposta i valori
combo['values'] = (1,2,3,4,5, "Voce 6")
# imposta l'oggetto selezionato
#combo.current(0)
combo.grid(row = 14, columnspan = 2, padx = 5 , pady = 5)


# BARRA MENU
mioMenu = Menu(miaFinestra)
# ADD_COMMAND
# tearoff = 0 --> non separa finestra
menuFile = Menu(mioMenu, tearoff = 0)
menuFile.add_command(label='Apri')
menuFile.add_command(label='Chiudi')
menuFile.add_separator()
menuFile.add_command(label='Uscita')
# ADD_CASCADE
mioMenu.add_cascade(label = "File", menu = menuFile)
miaFinestra.config(menu=mioMenu)


# PER FINIRE
# FINESTRE DI DIALOGO
#messagebox.showinfo('Titolo', 'Messaggio')
#messagebox.showwarning('Titolo', 'Messaggio pericolo')  #shows warning message
#messagebox.showerror('Titolo', 'Messaggio errore')    #shows error message
#ris = messagebox.askquestion('Message title','Message ASK QUERSTIO')
#print(YES-NO)
#ris = messagebox.askyesno('Message title','Message YES-NO')
#print(TRUE/FALSE)
#ris = messagebox.askyesnocancel('Message title','Message NO-CANCEL')
#print(TR/FA/NONE)
#ris = messagebox.askokcancel('Message title','Message OK-CANCEL')
#print(TR/FA)
#ris = messagebox.askretrycancel('Message title','Message RETRY-CANCEL')
#print(TR/FA)
miaFinestra.mainloop()
