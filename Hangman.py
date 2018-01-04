print(""" 

ooooo   ooooo                                                                          
`888'   `888'                                                                          
 888     888   .oooo.   ooo. .oo.    .oooooooo ooo. .oo.  .oo.    .oooo.   ooo. .oo.   
 888ooooo888  `P  )88b  `888P"Y88b  888' `88b  `888P"Y88bP"Y88b  `P  )88b  `888P"Y88b  
 888     888   .oP"888   888   888  888   888   888   888   888   .oP"888   888   888  
 888     888  d8(  888   888   888  `88bod8P'   888   888   888  d8(  888   888   888  
o888o   o888o `Y888""8o o888o o888o `8oooooo.  o888o o888o o888o `Y888""8o o888o o888o 
                                    d"     YD                                          
                                    "Y88888P'                                          
         """)

import random
import time

class bcolors:                    # kolory
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

draw1 = """
  +---+
  |   |
  0   |
      |
      |
      |
=======
"""
draw2 = """
  +---+
  |   |
  0   |
 /    |
      |
      |
=======
"""
draw3 = """
  +---+
  |   |
  0   |
 /|   |
      |
      |
=======
"""
draw4 = """
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=======
"""

draw5 = """
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=======
"""

draw6 = """
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=======
"""

plik = open("cap.txt")             #Otwieranie pliku z listą państwo-stolica
content = plik.readlines()
plik.close()

want_play = 1                   # zmienna, która może nam przerwać potem grę

while want_play == 1:           # Rozpoczęcie gry

    guess = 0
    print("Guess: ", guess)
    life = 6  
    print("Life: ", life, "\n")
    not_in_word = []                                # lista na błędne słowa/litery

    mystery0 = random.choice(content).upper()          # randomowa para państwo-stolica z pliku, wydobycie stolicy
    mystery0 = mystery0.split(" | ")
    mystery0[1] = mystery0[1].strip()
    capital = mystery0[1]
    country = mystery0[0]      

    mystery = list(capital)
    mystery2 = ["_"] * len(mystery)                 # zamiana nazwy stolicy na znaki
    if ' ' in mystery:
        for y in range(len(mystery)):               # spacje między słowami (jeśli więcej niż jedno) zamiast kreski
            if ' ' == mystery[y]:
                mystery2.pop(y)
                mystery2.insert(y, ' ')        
    print(" ".join(mystery2))

    start = time.time()                             # rozpoczyna odliczanie czasu
    bonus_time = 0

    letter = 1
    while letter == 1:                              # gracz wpisuje słowo/literę
        word_1 = input(bcolors.HEADER + "Write the word or letter: " + bcolors.ENDC).upper()
        guess += 1
        print("Guess: ",guess)

        if len(word_1) > 1:         # rozpoznaje słowo

            if list(word_1) == mystery:             # wygrana
                bonus_time += 5
                end = time.time()                   # Kończy odliczać czas i wskazuje wynik
                game_time = end - start - bonus_time
                date = time.strftime("%Y-%m-%d-%H:%M")
                print(bcolors.OKGREEN, "Winner!! Bonus time -5 seconds! You guessed after ", guess, 
                " letters. It took you: ", "%.2f" %(game_time), "second", bcolors.ENDC )
                name = input("What is your name? ")

                scorelist = [name, "|", str("%.2f" %(game_time)),"|", str(capital), "|",  str(date), "\n"]
                
                plik = open('highscore.txt', 'a')           # działania na pliku (utworzenie nowego, zapis str z danymi)
                plik = open('highscore.txt').read()
                plik = open('highscore.txt', 'a')
                plik.writelines(scorelist)
                plik.close()

                plik = open('highscore.txt').read()         #działania na pliku (otworzenie zapisów)
                plik2 = plik.split("\n")
                plik2.pop()              
                data1 = []
                for x in range(len(plik2)):                 
                    plik3 = plik2[x].split()
                    plik4 = plik3[0].split("|")
                    data1.append(plik4)

                not_sorted = True                           # sortowanie wg game_time - indeks [1] na scorelist
                while not_sorted:
                    not_sorted = False
                    for i in range(0, len(data1) -1):
                        if float(data1[i][1]) > float(data1[i+1][1]):
                            abc = data1[i]
                            data1[i] = data1[i+1]
                            data1[i+1] = abc
                            not_sorted = True
                print(data1)

                ask1 = input("Do you want to play again? (yes or no): ").upper()

                if ask1 == "YES":                   # gra od nowa
                    letter = 0

                else:
                    print("Have a nice day;)")
                    want_play = 0                   # przerywa grę
                    letter = 0


            else:                      # złe słowo
                
                life -= 2
                print("Life: ", life)
                print(" ".join(mystery2))
                not_in_word += [word_1]
                print("List of bad answers ", not_in_word)

                if life == 5:
                    print(draw1)
                elif life == 4:
                    print(draw2)
                elif life == 3:
                    print(draw3)
                elif life == 2:
                    print(draw4)
                elif life == 1:
                    print(draw5)
                    print("Hint! The capital of", country)    # wskazówka
                elif life < 1:                         # przegrana
                    print(draw6)
                    print(bcolors.FAIL, "Game over! Good answer is ", capital, bcolors.ENDC)  

                    ask2 = input("Do you want to play again? (yes or no): ").upper()

                    if ask2 == "YES":                   # gra od nowa
                        letter = 0

                    else:
                        print("Have a nice day;)")
                        want_play = 0                   # przerywa grę
                        letter = 0


        else:                           # rozpoznaje literę

            if word_1 in mystery:                       # poprawna litera

                for x in range(len(mystery)):           # index litery i wstawienie jej na odpowiednią kreskę

                    if word_1 == mystery[x]:
                        mystery2.pop(x)
                        mystery2.insert(x, word_1)
                
                print("Life: ", life)
                print(" ".join(mystery2))
                print("List of bad answers ", not_in_word)

                if mystery2 == mystery:                   # wygrana
                    end = time.time()                     # Kończy odliczać czas i wskazuje wynik
                    game_time = end - start
                    date = time.strftime("%Y-%m-%d %H:%M")
                    print(bcolors.OKGREEN, "Winner!! You guessed after ", guess, " letters. It took you: ", 
                    int(game_time), "second", bcolors.ENDC )
                    name = input("What is your name? ")

                    scorelist = [name, "|", str("%.2f" %(game_time)),"|", str(capital), "|",  str(date), "\n"]
                    
                    plik = open('highscore.txt', 'a')       # działania na pliku (utworzenie nowego, zapis str z danymi)
                    plik = open('highscore.txt').read()
                    plik = open('highscore.txt', 'a')
                    plik.writelines(scorelist)
                    plik.close()

                    plik = open('highscore.txt').read()     # działania na pliku (otworzenie zapisów)
                    plik2 = plik.split("\n")
                    plik2.pop()  

                    data1 = []
                    for x in range(len(plik2)):
                        plik3 = plik2[x].split()
                        plik4 = plik3[0].split("|")
                        data1.append(plik4)

                    not_sorted = True                       # sortowanie wg game_time - indeks [1] na scorelist
                    while not_sorted:
                        not_sorted = False
                        for i in range(0, len(data1) -1):
                            if float(data1[i][1]) > float(data1[i+1][1]):
                                abc = data1[i]
                                data1[i] = data1[i+1]
                                data1[i+1] = abc
                                not_sorted = True
                    print(data1)

                    ask3 = input("Do you want to play again? (yes or no): ").upper()

                    if ask3 == "YES":                      # gra od nowa
                        letter = 0

                    else:
                        print("Have a nice day;)")
                        want_play = 0                      # przerywa grę
                        letter = 0

            else:                       # zła litera

                life -= 1
                print("Life: ", life)
                print(" ".join(mystery2))
                not_in_word += [word_1]
                print("List of bad answers ", not_in_word)

                if life == 5:
                    print(draw1)
                elif life == 4:
                    print(draw2)
                elif life == 3:
                    print(draw3)
                elif life == 2:
                    print(draw4)
                elif life == 1:   
                    print(draw5)                            # wskazówka
                    print("Hint! The capital of", country)
                elif life < 1:
                    print(draw6)                            # przegrana
                    print(bcolors.FAIL, "Game over!! Good answer is ", capital, bcolors.ENDC)     

                    ask4 = input("Do you want to play again? (yes or no): ").upper()

                    if ask4 == "YES":                       # gra od nowa
                        letter = 0

                    else:
                        print("Have a nice day;)")
                        want_play = 0                       # przerywa grę
                        letter = 0


