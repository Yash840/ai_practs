
import random

secret_number = random.randint(1, 100)

def number_guessing_agent():

    low = 1
    high = 100
    attempts = 0

    while low <= high:

        guess = (low + high) // 2
        attempts += 1

        print("Agent guesses:", guess)

        if guess < secret_number:
            print("Feedback: Higher")
            low = guess + 1

        elif guess > secret_number:
            print("Feedback: Lower")
            high = guess - 1

        else:
            print("Feedback: Correct!")
            print("Number found:", guess)
            print("Total attempts:", attempts)
            return

number_guessing_agent()
