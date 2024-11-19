import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against computer answer.
def check_answer(guessed_number, computer_number):
    if guessed_number > computer_number:
        return "Too high."
    elif guessed_number < computer_number:
        return "Too low."
    elif guessed_number == computer_number:
        print(f"You got it! The answer was {computer_number}.")
        exit()
    
# Function to check the difficulty level
def check_difficulty():
    level=input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
        return turns
    elif level == "hard":
        turns = HARD_LEVEL_TURNS
        return turns
    else:
        print("Invalid input.")
        exit()


print("Welcome to the number guessing game!")

level_attempts=check_difficulty()
turns = 0
print("The program will randomly pick a number between 1 and 100...")
computer_number=random.randint(1,100)
print("The computer has picked a number.")

guessed_number=int(input("Make a guess: "))
print(f"You have {level_attempts} level_attempts remaining to guess the number.")
while turns < level_attempts:
    print(check_answer(int(guessed_number), computer_number))
    turns += 1
    if turns < level_attempts:
        attempts_remaining=level_attempts-turns
        print(f"Turns remaining: {attempts_remaining}")
        print("Guess again.")
        guessed_number=int(input("Make a guess: "))
    else:
        print("You've run out of guesses. You lose.")
        break
