import random


print("===== Number Guessing Game =====")


secret_number = random.randint(1,100)

attempts = 0


while True:

    guess = int(input("Guess number between 1-100: "))

    attempts += 1


    if guess == secret_number:

        print("Correct Guess!")
        print("Attempts:", attempts)
        break


    elif guess < secret_number:

        print("Too Low")


    else:

        print("Too High")
