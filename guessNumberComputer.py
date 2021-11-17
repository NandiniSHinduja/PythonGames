import random
def guess(x):
    random_number=random.randint(1,x)
    guess_number=int(input(f"Guess a number between 1 and {x}"))
    while random_number!=guess_number:
        if(random_number<guess_number):
            print("Guess is too high")
        elif(random_number>guess_number):
            print("Guess is too low")
        guess_number = int(input(f"Guess a number between 1 and {x}"))

    print("Yay, you guessed it correctly")
guess(10)
