# 2024 edition :-)
# This one handles ints and floats differently.

def choose_num():
    while True:
        num = input("Type a number: ")
        try:
            float(num)
            break
        except ValueError:
            print("That answer is not valid.")
    num = float(num)
    return num


def choose_operator():
    while True:
        symbol = input("Choose an operator (+ , - , * , /): ")
        if symbol not in ["+", "-", "*", "/"]:
            print("That answer is not valid.")
        else:
            break
    return symbol


def calculate(first_number, symbol, second_number):
    if symbol == "+":
        return first_number + second_number
    elif symbol == "-":
        return first_number - second_number
    elif symbol == "*":
        return first_number * second_number
    else:
        return first_number / second_number


def get_type(result):
    if result == int(result):
        return f"{result:.0f}"
    else:
        return f"{result:.7g}"  # Limit to 6 decimal digits, but cut off zeroes at the end


game_on = True
while game_on:
    num_1 = choose_num()
    calculation_continues = True
    while calculation_continues:
        operator = choose_operator()
        num_2 = choose_num()
        answer = calculate(num_1, operator, num_2)
        user_answer = get_type(answer)
        print(f"The answer is {user_answer}.")
        cont = input(f"Press 'y' to continue calculating with {user_answer} or any other key to start "
                     f"over: ").lower()
        if cont == "y":
            num_1 = answer
        else:
            break
            
