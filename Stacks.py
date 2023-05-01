my_list = []  # The main list where data will be added


def menu():  # The process of creating menu as stated on the activity
    print("*" * 39)
    print("*" * 5, "  My Stack Menu", " " * 11, "*" * 5)
    print("*" * 5, "  1.Push", " " * 18, "*" * 5)
    print("*" * 5, "  2.Pop", " " * 19, "*" * 5)
    print("*" * 5, "  3.Display Stack contents", " " * 0, "*" * 5)
    print("*" * 5, "  4.Exit", " " * 18, "*" * 5)
    print("*" * 39, "\n")


def stack():  # The process of creating a stack
    my_list = []
    return my_list


def push():  # : The process of adding (or inserting) a new element to the top of the stack
    my_list.insert(0, isi)


def pop():  # The process of deleting (or removing) an element from the top of stack
    my_list.pop()


def display():  # The process of displaying the data
    if len(my_list) == 0:
        print("Contents of the stack is\nStack Underflow!!!\n")
    else:
        print("\nContents of the stack is\n", *my_list)


def exit():  # The process of exiting the data
    quit()


menu() # To show the menu once

while True:
    option = int(input("Enter your Choice :: "))  # The user need to input the option

    try:
        if option == 1:  # To show the push method
            isi = int(input("Enter the number to be pushed into the stack :: "))
            push()
            print(f"The Number {isi} is pushed on the stack\n")
        elif option == 2:  # To show the pop method
            if len(my_list)-1 < 0:
                print("Contents of the stack is\nStack Underflow!!!\n")
                # If the stack is empty
            else:
                # To access the index and show it
                last_index = len(my_list) - 1
                index = my_list[last_index]
                pop()
                print(f"The popped element is: {index}\n")
        elif option == 3:  # To show the display method
            display()
        elif option == 4:  # To show the exit method
            exit()
        else:
            print("Input a number from 1 to 4")  # If the user inputs an int but not 1-4
    except ValueError:
        print("Input a valid number")  # If the user input an invalid input

