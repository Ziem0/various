while True:
    try:
        numbers = input('Type a number then space and choose system (2 for binary and 10 for decimal): ')
        split_numbers = numbers.split()
        number = int(split_numbers[0])
        system = int(split_numbers[1])
        result = ''
        number_to_string = str(number)
        # variables for binary--> decimal converter
        power = 0
        decimal = 0

        # decimal --> binary
        if system != 2 and system != 10:
            print ('Wrong system!')
        else:
            if system == 10:
                while number > 0:
                    result = str(number % 2) + result
                    # print (result)
                    number = number // 2
                print(" /------------\ ")
                print(" |",result,"--|--2| ")
                print(" \------------/ ")

            # binary --> decimal
            if system == 2:
                while len(number_to_string) > 0:
                    b = int(number_to_string[-1])
                    decimal = decimal + b * 2 ** power
                    power += 1
                    number_to_string = number_to_string[:-1]
                print(" /------------\ ")
                print(" |",decimal,"--|--10| ")
                print(" \------------/ ")


    except IndexError:
        print("ERROR! Please type --> number - space - 10 or 2 <-- !")
    except ValueError:
        print("ERROR! Use a numbers only!")


110

