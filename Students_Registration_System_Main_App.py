
# A function that displays the menu.
def menu_display():

    print("Please Select One of The Following:")
    print("\t(1) Add a New Student.")
    print("\t(2) Add a New Course.")
    print("\t(3) Add a New Grade.")
    print("\t(4) Print a Student's Transcript.")
    print("\t(0) Exit Program.")

    try:

        user_input = int(input("Enter Option: "))

        while user_input < 0 or user_input > 4:

            print("Wrong Input!\nEnter a Valid Option.")

            print("Please Select One of The Following:")
            print("\t(1) Add a New Student.")
            print("\t(2) Add a New Course.")
            print("\t(3) Add a New Grade.")
            print("\t(4) Print a Student's Transcript.")
            print("\t(0) Exit Program.")

            user_input = int(input("Enter Option: "))

        return user_input

    except ValueError:

        print("Invalid Input!\nEntered a Non Integer Value.")

        menu_display()


# Main Function
def main():

    user_input = menu_display()


# Calling Main Function
main()