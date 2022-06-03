#!/usr/bin/python3

def main():

choice ='0'
while choice =='0':
    print("Main Choice: Choose 1 of 5 choices")
    print("Choose 1 for something")
    print("Choose 2 for something")
    print("Choose 3 for something")
    print("Choose 4 for something")
    print("Choose 5 to go to another menu")

    choice = input ("Please make a choice: ")

    if choice == "5":
        print("Go to another menu")
        second_menu()
    elif choice == "4":
        print("Do Something 4")
    elif choice == "3":
        print("Do Something 3")
    elif choice == "2":
        print("Do Something 2")
    elif choice == "1":
        print("Do Something 1")
    else:
        print("I don't understand your choice.")

 def second_menu():
     print("This is the second menu")

 main()

 while loop_condition == True:
print("\nWelcome to Python Calculator!\n")
print("\nPlease enter a number for what you want to do.\n")
print("Enter 1 for addition.")
print("Enter 2 for subtaction.")
print("Enter 3 for division.")
print("Enter 4 for multiplication.")
print("Enter 5 to quit.\n")

main_input = int(input("What would you like to do? "))

if main_input == 5:
    loop_condition = False
    break
else:
    num1 = int(input("\nEnter your first number: "))
    num2 = int(input("Enter your sencond number: "))


    if main_input == 1:
        print(add(num1,num2))
    elif main_input == 2:
        print(sub(num1,num2))
    elif main_input == 3:
        print(div(num1,num2))
    elif main_input == 4:
        print(multi(num1,num2))

        def main():

choice =''
while choice !='0':
    choice = input ('Main choice: type: \nchoice 1: \nchoice 2: \nchoice 3: \nchoice 4:  \nchoice 5: \nchoice 6: ')
    print ('main menu 0')
    if choice =='1':
        print ('choice 1 - first level')
        choice = input ('Main choice: type: \nchoice 1: \nchoice 2:\nchoice 3 to go back:')
        if choice =='1':
            print ('choice 1:1 - end level menu')
            choice = input ('Main choice: type: \nchoice 1: \nchoice 2:\nchoice 3 to go back:')
        elif choice =='2':
            print ('choice 2:1 - end level menu')
            choice = input ('Main choice: type: \nchoice 1: \nchoice 2:\nchoice 3 to go back:')
        elif choice =='3':
            break
    elif choice =='2':
        print ('choice 2- first level')
        choice = input ('Main choice: type: \nchoice 1: \nchoice 2: \nchoice 3: \nchoice 4:  \nchoice 5: \nchoice 6: ')

    elif choice =='3':
        print ('choice 3- first level')
        choice = input ('Main choice: type: \nchoice 1: \nchoice 2: \nchoice 3: \nchoice 4:  \nchoice 5: \nchoice 6: ')

    elif choice =='4':
        print ('choice 4 - first level')
        choice = input ('Main choice: type: \nchoice 1: \nchoice 2: \nchoice 3: \nchoice 4:  \nchoice 5: \nchoice 6: ')

    elif choice =='5 - first level':
        print ('choice 5')
        joice = input ('Main choice: type: \nchoice 1: \nchoice 2: \nchoice 3: \nchoice 4:  \nchoice 5: \nchoice 6: ')
