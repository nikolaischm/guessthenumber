import random

def guess_number_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    
    print("Hello to the game!")
    print("Guess the number between 1 and 20!")

    while True:
        guess = int(input("Guess the number: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again...")
        elif guess > number_to_guess:
            print("Too high! Try again...")
        else:
            print(f"Concratulations! The number was {number_to_guess} !")
            print(f"Concratulations! You needed {attempts} tries.")
            break

if __name__ == "__main__":
    guess_number_game()
