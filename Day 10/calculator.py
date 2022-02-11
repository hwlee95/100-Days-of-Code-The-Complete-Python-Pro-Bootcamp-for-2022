# Python script for a simple calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def plus(first, second):
    return first + second

def minus(first, second):
    return first - second

def multiply(first, second):
    return first * second

def division(first, second):
    return first / second

def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))
    print("\n+\n-\n*\n/")
    to_continue = True
    while to_continue: 
        op = input("\nPick an operation: ")
        second_num = float(input("\nWhat's the next number?: "))
        result = 0.0
        if op == "+":
            result = plus(first_num, second_num)
        elif op == "-":
            result = minus(first_num, second_num)
        elif op == "*":
            result = multiply(first_num, second_num)
        elif op == "/":
            result = division(first_num, second_num)
        else:
            print("Invalid operation.")
        print(f"\n{first_num} {op} {second_num} = {result}")

        if input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            first_num = result
        else:
            to_continue = False
            calculator()

if __name__ == "__main__":
    calculator()