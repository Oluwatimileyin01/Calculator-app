# import math
# print("""
#             **CALCULATOR**

# choose an operation from the list:

#         1. Addition
#         2. Subtraction
#         3. Division
#         4. Multiplication
#         5. Modulo
#         6. Floor Division
#         7. Exponential
#         8. Square root
#         9. Cube root
#         10. log
#         11. Exponential function(e)
#         12. Factorial

#     """)
# operation = input("Input your choice operation: ")

# if operation == "1":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) + int(second_val))
# elif operation == "2":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) - int(second_val))
# elif operation == "3":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val)/int(second_val))
# elif operation == "4":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) * int(second_val))
# elif operation == "5":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) % int(second_val))
# elif operation == "6":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) // int(second_val))
# elif operation == "7":
#     first_val = input("Enter first_val: ")
#     second_val = input("Enter second_val: ")
#     print(int(first_val) ** int(second_val))
# elif operation == "8":
#     number = input("Enter number: ")
#     print(math.sqrt(int(number)))
# elif operation == "9":
#     number = input("Enter number: ")
#     print(math.pow(int(number),(1/3)))
# elif operation == "10":
#     number = input("Enter number: ")
#     base = input("Enter base number: ")
#     print(math.log(int(number),int(base)))
#     # print(result)
# elif operation == "11":
#     number = input("Enter number: ")
#     print(math.exp(int(number)))
# elif operation == "12":
#     number = input("Enter number: ")
#     print(math.factorial(int(number)))
# elif operation == "13":
#     number = input("Enter number")
#     print(math.())
# else:
#     print("Error")





                        ## CALCULATOR using FUNCTION




import re
import math
import sys
def Addiction():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 + user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Addiction()
    # else:
        # print("Result = ",result)
    # finally:
    #     user = (input("Press 'Enter' to repeat and '1' to exit:  "))
    #     if user == "1":
    #         sys.exit()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input, input a number")
        landing_page()

def Substraction():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 - user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Substraction()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Multiplication():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 * user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number")
        Multiplication()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Division():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 / user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Division()
    except ZeroDivisionError:
        print("your division can't be zero")
        Division()

    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Modulo():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 % user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Modulo()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() .capitalize()== "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Floor_Division():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 // user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Floor_Division()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Exponential():
    try:
        user1 = int(input("Enter First Val1 "))
        user2 = int(input("Enter First Val2 "))
        result = user1 ** user2
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Exponential()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Square_root():
    try:
        user1 = int(input("Enter Val "))
        result = math.sqrt(int(user1))
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Square_root()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def log():
    try:
        user1 = int(input("Enter number "))
        base = input("Enter base number: ")
        result = math.log(int(user1),int(base))
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        log()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def cube_root():
    try:
        user1 = int(input("Enter number "))
        result = math.pow(int(user1),(1/3))
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        cube_root()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def Exponential_fuction():
    try:
        user1 = int(input("Enter number "))
        result = math.exp(int(user1))
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        Exponential_fuction()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()
        

def Factorial():
    try:
        user1 = int(input("Enter number "))
        result = math.factorial(int(user1))
        print("Result = ",result)
    except ValueError:
        print("Invalid input, input a number ")
        factorial()
    user = input("press A to perform another opration or D to dismiss ")
    if user.capitalize() == "A":
        landing_page()
    elif user.capitalize() == "D":
        sys.exit
    else:
        print("Invalid input")
        landing_page()

def landing_page():
    print("""""")
    print("**CALCULATOR**  \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulo \n6. Floor Division \n7. Exponential \n8. Square root \n9. log \n10. Cube root \n11. Exponential function(e) \n12. Factorial  \nE. Exist")
    operation = input("choose    ")
    choice_operation = ["1", "2", "3","4", "5", '6', "7", "8"," 9", "10", "11", "12", "E"]
    while operation not in choice_operation:
        print("Invalid Input, Try again.")
        operation = input("choose    ")
    if operation == "1":
        Addiction()
    elif operation == "2":
        Substraction()
    elif operation == "3":
        Multiplication()
    elif operation == "4":
        Division()
    elif operation == "5":
        Modulo()
    elif operation == "6":
        Floor_Division()
    elif operation == "7":
        Exponential()
    elif operation == "8":
        Square_root()
    elif operation == "9":
        log()
    elif operation == "10":
        cube_root()
    elif operation == "11":
        Exponential_fuction()
    elif operation == "12":
        Factorial()
    elif operation.capitalize() == "e":
        sys.exit()

landing_page()

