import random
print("Welcome to Guess the Number Game \n You have 3 chances ")
ub = int(input("Enter the upper limit:"))
lb = int(input("Enter the lower limit:"))
number = random.randrange(ub,lb)
chance = 0
while chance<3:
    chance += 1
    guess = int(input("\nGuess the number: "))
    if number == guess:
        print("“Congrat’s” \n You Guessed the number in {} chances".format(chance))
        break
    elif number > guess:
        print("“have one more try.Your guess was too small”")
    elif number < guess:
        print("“have one more try.Your guess was too high!")
if chance >= 3 and number < guess or number > guess:
    print("\nMaximum No. of Chances reached")
    print("Better Luck Next Time!")