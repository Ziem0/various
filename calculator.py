import sys
def valid_invalid(param):
    try:
     param = int(param)
    except ValueError:
     print ("So see you next time!")
     sys.exit(0)


def addidtion(a, b):
  return a+b
def subtraction(a, b):
  return a-b
def multiplication(a, b):
  return a*b
def division(a, b):
  if b==0:
    return "0? Are you joking?"
  else:
    return a/b
def modulo(a, b):
  if a>b:
    return a%b
  else:
    return '0'

def main():
    if (True):
        a_input = input("Enter a number (or a letter to exit): ")
        valid_invalid(a_input)
        a_input = int(a_input)

        x_input = input("Enter an operation: ")
    while x_input !="+" and x_input !="-" and x_input !="*" and x_input !="/" and x_input !="%":
        x_input = input("Incorrect sign! Try again: ")

    if (True):
        b_input = input("Enter another number (or a letter to exit): ")
        valid_invalid(b_input)
        b_input = int(b_input)


    if x_input == "+":
        result = addidtion(a_input, b_input)
    elif x_input == "-":
        result = subtraction(a_input, b_input)
    elif x_input == "*":
        result = multiplication(a_input, b_input)
    elif x_input == "/":
        result = division(a_input, b_input)
    elif x_input == "%":
        result = modulo(a_input, b_input)


    print("Search result: ", result)
    print('\n'*2)
    again()

def again():
    once_again = input('''
Once again?
Type Y for YES or N for NO.
''')

    if once_again.upper() == 'Y':
        main()
    elif once_again.upper() == 'N':
        print('Good for you..')
    else:
        print('Y or N ?!')
        again()

main()
