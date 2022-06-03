#!/usr/bin/python3
#Lezione del 01 Dicembre 2018
#Menu in Python
#Gestione di un archivio di aziende(nominativo, nazione, fatturato)
#Uso di liste, funzioni...
import os

#definizione di una PROCEDURA
def Visualizza_Menu(): 
    print("\n\n")
    print("Menu dei comandi:")
    print(" 1 - Aggiungi Azienda")
    print(" 2 - Elimina Azienda")
    print(" 3 - Visualizza elenco delle Aziende")
    print(" ...  ")
    print("C - Clear screen")
    print("Q - Quit")
    #non compare il RETURN

#definizione di una FUNZIONE
def Aggiungi_Azienda():
    azienda=[] #è la lista corrispondente all'azienda che sto aggiungendo
    nominativo=input("Nominativo Azienda ---> ")
    nazione=input("Nazione Azienda ---> ")
    fatturato=input("Fatturato Azienda ---> ")
    azienda.append(nominativo)
    azienda.append(nazione)
    azienda.append(fatturato)
    archivio.append(azienda)
    return True
    
def Visualizza_Archivio():
    print(archivio)

#inizio del corpo del programma
archivio=[]
while (True):
    Visualizza_Menu()
    scelta=input("Scelta ---> ")
    if scelta=="1":
        Aggiungi_Azienda()
    elif scelta=="2":
        pass
    elif scelta=="3":
        Visualizza_Archivio()
    elif scelta=="C":
        os.system("clear")
    elif scelta=="Q":
        print("\n\nbye...bye...\n\n")
        exit(1) #esci dal ciclo while
                   








