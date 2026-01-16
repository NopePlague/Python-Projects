import random

def play_game():
    while True:
        play_one_game()

        choice = input("Play again (y/n): ").lower()
        if choice != "y":
            print("Thank you for playing.")
            break

def play_one_game():
    secret = generate_number()
    print(secret)
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        if get_user_guess(secret):
            print(f"Correct! You won.")
            return

    print("Game over! The number was:", secret)

def generate_number():
    secret=random.randint(1,100)
    return secret

def get_user_guess(secret):
    i=0
    while True:
        user_input = input("Enter a number: ")

        if user_input.isdigit() and (int(user_input)>0 and int(user_input)<=100):
            guess = int(user_input)
            return check_guess(secret, guess)
        else:
            print("Invalid Input", i)
            i+=1
            if i>=5:
                return False

def check_guess(secret, guess):
    return secret==guess

play_game()