from art import logo


def get_number():
    """Get a number from the user"""
    while True:
        num = input("Type a number: ")
        try:
            return float(num)
        except ValueError:
            print("Error. Try again.")


def get_operator():
    """Get an operator (+, -, *, /) from the user."""
    while True:
        print("+\n-\n*\n/")
        sign = input("Choose an operator: ")
        if sign in ["+", "-", "*", "/"]:
            return sign
        else:
            print("Error. Try again.")


def perform_operation(num_1, sign, num_2):
    """Perform a mathematical operation on two numbers."""
    while True:
        if sign == "+":
            answ = num_1 + num_2
            return answ
        elif sign == "-":
            answ = num_1 - num_2
            return answ
        elif sign == "*":
            answ = num_1 * num_2
            return answ
        elif sign == "/":
            if num_2 == 0:
                print("Error. Division by zero not allowed.")
                return None
            else:
                answ = num_1 / num_2
                return answ

# main loop starts here


print(logo)
while True:
    first_num = get_number()
    inner_loop = True
    while inner_loop:
        if first_num is not None:
            operator = get_operator()
            if operator:
                second_num = get_number()
                if second_num is not None:
                    answer = perform_operation(first_num, operator, second_num)
                    if answer is not None:
                        print(f"The answer is {first_num} {operator} {second_num} = {answer}")
                        continue_or_not = input(f"Press \"y\" to continue calculating with {answer} or press any other "
                                                f"key to start over: ").lower()
                        if continue_or_not == "y":
                            first_num = answer
                        else:
                            inner_loop = False
