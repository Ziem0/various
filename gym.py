#!/usr/bin/python3
import random

print("Welcome to GYM")

questions=["Are you under 14? ","Are you a sauna user? ",
            "Are you a student? ","Are you a man? "]

ascart_20=[
" _______ _______    _      ________________________ _       ________________",
"/ ___   |  __   )__|_|___  \__   __|__   __(  ____ \ \    /(  ____ \__   __/",
"\/   )  | (  )  (  _____/     ) (     ) (  | (    \/  \  / / (    \/  ) (",
"    /   ) | /   | (|_|__      | |     | |  | |     |  (_/ /| (__      | |",
"  _/   /| (/ /) (_____  )     | |     | |  | |     |   _ ( |  __)     | |",
" /   _/ |   / | /\_|_|) |     | |     | |  | |     |  ( \ \| (        | |",
"(   (__/\  (__) \_______)     | |  ___) (__| (____/\  /  \ \ (____/\  | |",
"\_______(_______)  |_|        )_(  \_______(_______/_/    \(_______/  )_("]

ascart_5=[
" _______    _      ________________________ _       ________________",
"(  ____ \__|_|___  \__   __|__   __(  ____ \ \    /(  ____ \__   __/",
"| (    \(  _____/     ) (     ) (  | (    \/  \  / / (    \/  ) (   ",
"| (____ | (|_|__      | |     | |  | |     |  (_/ /| (__      | |   ",
"(_____ \(_____  )     | |     | |  | |     |   _ ( |  __)     | |   ",
"      ) )\_|_|) |     | |     | |  | |     |  ( \ \| (        | |   ",
"/\____) )_______)     | |  ___) (__| (____/\  /  \ \ (____/\  | |   ",
"\______/   |_|        )_(  \_______(_______/_/    \(_______/  )_(   "]

ascart_15=[
"  __   _______    _      ________________________ _       ________________",
" /  \ (  ____ \__|_|___  \__   __|__   __(  ____ \ \    /(  ____ \__   __/",
" \/) )| (    \(  _____/     ) (     ) (  | (    \/  \  / / (    \/  ) (   ",
"   | || (____ | (|_|__      | |     | |  | |     |  (_/ /| (__      | |   ",
"   | |(_____ \(_____  )     | |     | |  | |     |   _ ( |  __)     | |   ",
"   | |      ) )\_|_|) |     | |     | |  | |     |  ( \ \| (        | |   ",
" __) (/\____) )_______)     | |  ___) (__| (____/\  /  \ \ (____/\  | |   ",
" \____|______/   |_|        )_(  \_______(_______/_/    \(_______/  )_(  "]

ascart_10=[
"  __   _______    _      ________________________ _       ________________",
" /  \ (  __   )__|_|___  \__   __|__   __(  ____ \ \    /(  ____ \__   __/",
" \/) )| (  )  (  _____/     ) (     ) (  | (    \/  \  / / (    \/  ) (   ",
"   | || | /   | (|_|__      | |     | |  | |     |  (_/ /| (__      | |   ",
"   | || (/ /) (_____  )     | |     | |  | |     |   _ ( |  __)     | |   ",
"   | ||   / | /\_|_|) |     | |     | |  | |     |  ( \ \| (        | |   ",
" __) (|  (__) \_______)     | |  ___) (__| (____/\  /  \ \ (____/\  | |   ",
" \____(_______)  |_|        )_(  \_______(_______/_/    \(_______/  )_(   "]

answers=["Sorry you are to young, bye",ascart_20, ascart_5,ascart_15, ascart_10]

jokes=["My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away",
        "I heard women love a men in uniform. Cant wait to start working at McDonald's",
        "A naked woman robbed a bank, nobody could remember her face",
        "I'm selling my talking parrot because yesterday the bastard tried to sell me",
        "A wife is like a hand granade. Take off the ring and say goodbye to your house"]

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

i=0
while i<(len(answers)):
    while i<(len(questions)):
        user_answer=input(B + questions[i])
        print(O + random.choice(jokes) +R)
        if user_answer.upper()=="YES":
            if i>0:
                for arg in answers[i]:
                    print(arg)
            else:
                print(answers[i])
            i=len(answers) # => quit main loop condition
            break
        elif user_answer.upper()=="NO":
            break
        print(G + "Please answer YES or NO",random.choice(jokes))
    if i==len(answers)-1:
        for arg in answers[i]:
            print(arg)
        break
    i+=1
