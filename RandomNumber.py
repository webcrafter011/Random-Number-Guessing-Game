import random

# Greeting the user
user_name = input("Enter your name: ")

input(f"Hello {user_name}, welcome to this fun little random number guessing game.\nPress Enter to continue.")

# Get valid lower and upper limits
while True:
    try:
        lower_limit = int(input("Enter lower limit: "))
        upper_limit = int(input("Enter upper limit: "))
        if lower_limit >= upper_limit:
            print("Lower limit must be less than upper limit. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter valid integers for the limits.")

# Generate the random number
number_to_guess = random.randint(lower_limit, upper_limit)
chances = 7

# Start the guessing game
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input("Please Enter your Guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        guess_counter -= 1  # Do not count invalid attempts
        continue

    if my_guess == number_to_guess:
        print(f"Congratulations! The number is {number_to_guess}, and you found it in {guess_counter} attempt(s)! 🎉")
        break
    elif my_guess > number_to_guess:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")

    if guess_counter == chances:
        print(f"Oops, you're out of chances! The number was {number_to_guess}. Better luck next time!")
