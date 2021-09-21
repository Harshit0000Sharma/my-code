from random import randint
number = randint(1, 1000)
user_guess = None
guesses = 0
while user_guess != number:
    try:
        user_guess = int(input("enter your guess"))
        guesses += 1
        if user_guess == number:
            print("you guessed it right")
        else:
            print("you guessed it wrong")
            if user_guess > number:
                print("think of small number")
            else:
                print("think of a big number")
    except ValueError:
        pass
        print(f"you guessed in {guesses} turn")
with open("high_score.txt", "r") as f:
    high = int(f.read())
if(guesses < high):
    print("You have just broken the high score!")
    with open("high_score.txt", "w") as f:
        f.write(str(guesses))
