#!usr/bin/python3
import random
import sys
import time

# ascII arts
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
earth = G + "(@)" + W
rocket = O + "\b-<#=#<" + W
end_of_the_world = G + "(." + R + "\BOOM!/" + O + ",#<" + W

print("\nYour mission is to save the world:", earth,
      "\nHurry up, lethal rocket: ", rocket, "is approaching.")

# reading cities and countries from file
with open('cap.txt', "r") as from_file:
    capitals_2 = from_file.read().splitlines()

while True:  # main loop

    # setting variables
    random_line = random.choice(capitals_2)
    country_and_capital = random_line.split(" | ")
    city = country_and_capital[1].upper()
    city_list = []
    letters = []
    wrong = []
    lives = 5
    count = 0
    guessed = False
    start_time = time.time()
    for i in city:
        city_list.append(i)
        letters.append('_')


# cheat mode => display city name
    if (len(sys.argv) - 1):
        if sys.argv[1] == "demo":
            print(R + "\nGuessed letters:", *city, "<-- cheat mode ON" + W)

    while (lives > 0 and not guessed):  # guessing loop
        if lives == 1:
            print("Hint: this is capital of", country_and_capital[0].upper())
        print("\nLives:", lives, earth, (lives - 1) * " ", rocket,
              "\nGuessed letters:", *letters, "  Wrong characters:", *wrong)

        w_or_l = input("\n(W)ord or (L)etter: ").upper()
        # decision: word guessing, or another letter

        if (w_or_l == "W"):  # word guessing
            count += 1
            word = input("guess city: ").upper()
            if (word == city):  # quit from the "guessing loop"
                guessed = True  # (by condition checking)
            else:
                lives -= 2  # punishment
                print("You are wrong! ")

        elif (w_or_l == "L"):  # letter guessing
            count += 1
            char = input("type a letter: ").upper()
            while len(char) < 2:
                if char in city:  # adding GOOD letter
                    for i in range(0, len(city)):
                        if (city[i] == char):
                            letters[i] = char
                    break
                else:  # adding WRONG letter to list + punishment
                    lives -= 1
                    if char not in wrong:
                        wrong.append(char)
                    break
            else:
                print("Too many letters.")
            if (letters == city_list):  # quit from the "guessing loop"
                guessed = True  # (by condition checking)

    if (guessed):
        guessing_time = round(time.time() - start_time)
        print(G + "\nCongratulations, you saved the world in", count,
              "letters and", guessing_time, "seconds" + W)

    if (lives < 1):
        print(R + "\nYou are dead: ", end_of_the_world)

    again = input("Thank you for playing. Enter Q to quit the program: ").upper()
    if again == 'Q':
        break
