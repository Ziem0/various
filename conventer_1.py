def binary_to_decimal(binary):
    decimal = 0
    while len(binary) > 1:
        counter = 1                      #11011  1011  11
        for sign in binary:
            counter *= 2                 #32     16     4
        decimal += counter / 2           #16     8      2 #3
        if binary[0] == '1':
            binary = binary[1:]           #1011   011   1
            binary = binary.lstrip('0')          #11
        if len(binary) == 1:
            if binary[-1] == '1':
                decimal += 1                            #3

    line = '-'*(len(str(decimal)))
    print(" /"+line+"-----\ ")
    print(" |",int(decimal),"| 10 |")
    print(" \ "+line+"----/ ")


def decimal_to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2

    line = '-'*(len(result))
    print(" /"+line+"-------\ ")
    print(" |",result,"|  2 |")
    print(" \ "+line+"------/ ")


def binary_validation(binary):
    if all(i == '0' or i =='1' for i in binary):
        binary_to_decimal(binary)
    else:
        print("Use only '1' or '0' !")


def main():
    while True:
        try:
            numbers = input('Type a number then space and choose system (2 for binary and 10 for decimal): ')
            split_numbers = numbers.split()
            number = int(split_numbers[0])
            system = split_numbers[1]
            binary = str(number)
            if system == '2':
                binary_validation(binary)
            elif system == '10':
                decimal_to_binary(number)
            else:
                print ('Wrong system!')

        except IndexError:
            print("ERROR! Please type --> number - space - 10 or 2 <-- !")
        except ValueError:
            print("ERROR! Use a numbers only!")

main()

# logika na dec
# 10101   21  --- 16(2(01),4,8,16) + 4(zero pomijam) + zero pomijam + 1(bo jeden na koncu)
# 110110 - 54 (32 + 16 + 4 + 2)

#logika na bin
# 21 - 10101 --- 16 4 1
# 2 10
# 4 100
# 8 1000
# 16 10000
# 11011011
# 128 64 16 8 2 1  = 219
