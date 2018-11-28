from random import randint
low_number = input("Enter a number: ")
high_number = input("Enter a number greater than " + low_number + ": ")
counter = 0
i = randint(int(low_number), int(high_number))
guess = 0

while guess != i:
    guess = input("Make a guess between " + str(low_number) + " and " + str(high_number) + ": ")
    if int(guess) < int(i):
        print("higher")
        low_number = guess
    elif int(guess) > int(i):
        print("lower")
        high_number = guess
    else:
        print("Congratulations, it took you " + str(counter) + " guesses to get it")
        break
    counter = counter + 1