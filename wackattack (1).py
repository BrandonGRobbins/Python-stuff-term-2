#Brandon Robbins
#Jared McMahon
#11-2-18
#Period  4-5
import random
def main():
    print(" Welcome to Number Guesser !")
    print("")
    print("I will pick a number between 1 and 100.")
    print("Try to guess my number in a few guesses as possible.")
    print("I will give hints along the way")
    print("")
    print("")
    print("Ok, ive picked my number")

def credit():
    print("""This game was built by  Brandon and Jared
Thank you for playing
Why did you even check the credits?
:)""")
#running the base game
def run():
    hidden = random.randrange(0,100)
    count = 1
    guess = 0
    while guess != hidden:
        guess =int(input("What is your guess "))
        if guess < hidden:
            print ("to low")
            count += 1
        if guess > hidden:
            print ("to high")
            count += 1
        elif guess == hidden:
            print ("That's it")
            print("you guessed my number in ",count," tries")
            break
        elif count > 5:
            print("you've tried too many times!")
            break

#changing the number range
def runWchange():
    minimum = int(input("minimum value"))
    maximum = int(input("maximum value"))
    hidden = random.randrange(minimum,maximum)
    count = 1
    guess = 0
    while guess != hidden:
        guess =int(input("What is your guess "))
        if guess < hidden:
            print ("to low")
            count += 1
        if guess > hidden:
            print ("to high")
            count += 1
        if guess == hidden:
            print ("That's it")
            print("you guessed my number in ",count," tries")
            break
        if count >5:
            print("you've tried too many times!")
            break

#allowing you to quit
while True:

            
    main()

#main menu
    inputt=input("""Quit=q
    Credits=c
    Play=p
    Range Select=r
    """)
    if inputt == "p":
        run()
    if  inputt == "c":
        credit()
    if inputt == "r":
        runWchange()
    if inputt == "q":
        break





print("press enter to exit")
input()
