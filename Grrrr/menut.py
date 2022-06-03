#!/usr/bin/python3

import os

def Back_up():
    print("Starting backup...")
    return False

def Usr_Menager():
    print ("Starting user management...")
    return False

def Reboot_Server():
    print("Rebooting the server...")
    return False

print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the server")
print ("C. Clean the menu")
print ("E. Exit")
print (30 * '-')

scelta=input("Enter your choice: ")

while (True):
    if scelta=="1":
        Back_up()
    elif scelta=="2":
        Usr_Menager()
    elif scelta=="3":
        Reboot_Server()
    elif scelta=="C":
        os.system("clear")
    elif scelta=="E":
        print("")
        exit(1)
