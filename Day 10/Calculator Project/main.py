from art import logo
def add(n1, n2):
    return n1 + n2

def multiply(n1,n2):
    return n1 * n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

calc_map ={
    "*" : multiply,
    "-" : subtract,
    "+" : add,
    "/" : divide,
}

def calculator():
    print(logo)
    n1 = int(input("enter a number"))
    calculator_on = True
    while calculator_on:
        print("x\n/\n+\n-\n")
        operation = input("enter an operation")
        if operation not in calc_map:
            print("x\n/\n+\n-\n")
            operation = input("please enter a valid operation")

        n2 = int(input("enter second number"))
        if n2 == 0 and operation == "/":
            n2 = int(input("please enter a non zero number"))
        n1 = calc_map[operation](n1, n2)

        prompt = input(f"Type 'y' to continue with {n1} or 'n' to start a new calculation or 'x' to exit.")
        if prompt == 'x':
            return print("thank you")
        if prompt == 'y':
            calculator_on = True
        if prompt == 'n':
            calculator_on = False
            calculator()

calculator()
