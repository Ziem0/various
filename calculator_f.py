
def read_number(exit_on_alpha=False):
    input_msg = 'Enter a number :'
    if exit_on_alpha:
        input_msg += '(or a letter to exit):'

    arg = input(input_msg)
    while not arg.isdigit():
        if exit_on_alpha and arg.isalpha():
            exit()
        arg = input('Invalid number! ' + input_msg)
    return int(arg)


def read_operator(operators):
    operator = input('Enter an operation: ')
    while operator not in operators:
        operator = input('Invalid sign! Enter an operation: ')
    return operator


def evaluate(num1, num2, operatora):
    result = None

    if operatora == '+':
        result = num1 + num2
    elif operatora == '-':
        result = num1 - num2
    elif operatora == '*':
        result = num1 * num2
    elif operatora == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("You can't divide by zero!")
    return result


def main():

    while True:

        arg1 = read_number(exit_on_alpha=True)

        operator = read_operator(['+', '-', '*', '/'])

        arg2 = read_number()

        result = evaluate(arg1, arg2, operator)

        print("Result: " + str(result))


if __name__ == '__main__':
    main()
