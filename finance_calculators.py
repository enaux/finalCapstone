"""
This program contains two financial calculators.
The user chooses which calculator they wish to use.

The first calculator allows the user to calculate the interest earned on an investment.
The second calculator allows the user to calculate the monthly repayments on a home loan.

The body of the program is nested within a while-loop to allow the user to continue
making calculations until they decide to exit the program.

The financial calculators are coded using nested 'if-elif' statements to respond
to the user's choice of calculator.
"""


# Import module for performing calculations required in program.
import math

# Set initial state of 'done' variable to False.
# User will choose to keep or modify variable at the end of the first while-loop iteration.
# This allows user to continue or exit the program.
done = False

while not done:

    # Print a welcome message.
    print("Welcome to our Financial Calculators.")
    print("Choose your desired option below.")
    print("-"*90)

    # Print the user menu, and ask the user to choose a calculator.
    print("investment\t- to calculate the amount of interest "
          "you'll earn on your investment")
    print("bond\t\t- to calculate the amount you'll have to pay on a home loan")
    print("-"*90)
    calculator_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:\t")

    # Convert the user input to lowercase to form usable code for the rest of the program.
    calculator_choice = calculator_choice.lower()

    # while-loop to ensure that the user correctly selects one of the options: 'investment' or 'bond'.
    while (calculator_choice != "investment"):
        if (calculator_choice == "bond"):
            break
        print()
        print("\t\t\t***** Invalid entry *****")
        print()
        calculator_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed:\t")
        calculator_choice = calculator_choice.lower()

    # Confirm the chosen calculator for the user.
    print()
    print(f"You have chosen the {calculator_choice.title()} Calculator.\n")


    # Investment Calculator
    if calculator_choice == "investment":

        # Seek user input of the principal amount.
        P = int(input("Enter the amount of money you will deposit:\t"))
        
        # Seek user input of the interest rate.
        i = int(input("Enter the % interest rate (as a number only, e.g. for 5% enter '5'):\t"))

        r = i/100

        # Seek user input of the length of investment.
        t = int(input("How many years do you plan to invest for?\t"))

        # Seek user input of the type of interest to be calculated.
        print("Will the interest be calculated as simple interest "
            "or compound interest?")
        interest = input("Please enter either 'simple' or 'compound' to proceed:\t")
        interest = interest.lower()

        # while-loop to ensure user correctly selects one of the options: 'simple' or 'compound'.
        while (interest != "simple"):
            if (interest == "compound"):
                break
            print()
            print("\t\t\t***** Invalid entry *****")
            print()
            interest = input("Please enter either 'simple' or 'compound' to proceed:\t")
            interest = interest.lower()

        # Calculator for simple interest.
        if interest == "simple":
            A = P*(1+(r*t))
        # Calculator for compound interest.
        elif interest == "compound":
            A = P*math.pow((1+r),t)

        # Print the results for the user.
        print("-"*90)
        print(f"The total sum at the end of the investment period will be £{A}.")
        print(f"The amount of interest earned on this investment will be £{(A-P)}.")
        print("-"*90)
            

    # Bond Calculator  
    elif calculator_choice == "bond":

        # Seek user input of the house value.
        P = int(input("Enter the present value of your house:\t"))

        # Seek user input of the interest rate on the loan, and calculate the monthly rate.
        annual_interest = int(input("Enter the annual interest rate on your loan:\t"))
        i = (annual_interest/100)/12

        # Seek user input of the number of months to repay the loan.
        n = int(input("Enter the number of months you will take to repay the loan:\t"))

        # Calulator for monthly repayment cost
        repayment = (i*P)/(1-(1+i)**(-n))

        # Print the results for the user.
        print("-"*90)
        print(f"Your monthly repayment will be £{repayment}.")
        print("-"*90)

    # Allow user to choose whether to continue or exit.
    print()
    print("Do you wish to make another calculation?")
    print()
    user_choice = input("Please enter 'yes' to continue, or 'no' to exit the calculator:\t")
    user_choice = user_choice.lower()

    # while-loop to ensure the user enters a valid option.
    while (user_choice != "yes"):
        if (user_choice == "no"):
            break
        print()
        print("\t\t\t***** Invalid entry *****")
        print()
        user_choice = input("Please enter 'yes' to continue, or 'no' to exit the calculator:\t")
        user_choice = user_choice.lower()

    # If user chooses to continue, print some lines and spaces for readability.
    if user_choice == "yes":
        print()
        print("-"*90)
        print("-"*90)
        print()
    
    # If user chooses to exit, set 'done' to exit the while-loop.
    elif user_choice == "no":
        done = True


# Closing statement.
print()
print("-"*90)
print()
print("Thank you for using our calculator.")
print("Goodbye.")
print()
