# A simple calculator to perform basic airthmetic operations
# Prompt the user to input two numbers and and an operator
# Display the Result.

try :
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    op = input("Enter an operator(+,-,*,/,%): ")

    match op:
        case '+': print("Result:", a+b)
        case '-': print("Result:", a-b)
        case '*': print("Result:", a*b)
        case '/': print("Result:", a/b)
        case '%': print("Result:", a%b)
        case _: print("Please enter valid operators!")

except ValueError:
    print("Please enter numeric values only!!")