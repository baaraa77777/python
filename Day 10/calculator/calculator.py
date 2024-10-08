from art import calc_logo
from clear import clear_screen

def add(n1 ,n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 *n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-":subtract,
    "*": multiply,
    "/":divide
}
def calculator():
    print (calc_logo)

    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the next number: "))

        calculation_funtion = operations[operation_symbol]  
        answer = calculation_funtion(num1, num2)

        print( f"{num1} {operation_symbol} {num2} = {answer} ")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear_screen()
    calculator()
calculator()
