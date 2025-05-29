import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

basic_operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(art.logo)
    should_continue = True
    first_number = int(input("What is your first number? \n"))


    while should_continue:
        operator = input("Choose your operator\n'+'\n'-'\n'*'\n'/'\n")
        second_number = int(input("What is your second number? \n"))
        first_operation = basic_operations[operator](first_number, second_number)
        result = first_operation
        print(f"{first_number} {operator} {second_number} = {result}")
        continue_calculation = input(f"Do you want to continue with {result}? Type 'y' or 'n'").lower()
        print(continue_calculation)

        if continue_calculation == "y":
            first_number = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()


