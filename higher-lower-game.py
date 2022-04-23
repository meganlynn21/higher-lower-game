from art import logo
from art import vs
from game_data import data
import random
import os

# Retrieve random values from game_data dictionary
first_choice = random.choice(data)
second_choice = random.choice(data)
score = 0


def main():
    print(logo)

    # Compare the amount of followers from the list of dictionaries and
    # take string input as first choice A or second choice B
    def compare(string):
        a_choice = "A"
        b_choice = "B"
        if string == a_choice and first_choice['follower_count'] > second_choice['follower_count']:
            print("Your Right!")
            return True
        elif string == a_choice and first_choice['follower_count'] < second_choice['follower_count']:
            return False
        elif string == b_choice and first_choice['follower_count'] < second_choice['follower_count']:
            print("Your Right!")
            return True
        elif string == b_choice and first_choice['follower_count'] > second_choice['follower_count']:
            return False

    # Create a count variable to hold the score and create a loop to keep the game going
    def play_again():
        should_continue = True

        while should_continue:
            global second_choice
            global first_choice
            first_choice = second_choice
            second_choice = random.choice(data)

            while first_choice == second_choice:
                second_choice = second_choice.random(data)

            print("Which of the following has more followers?")
            print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
            print(vs)
            print(
                f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
            a_or_b = input("Who has more followers? Type 'A' or 'B': ")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)

            if compare(a_or_b) == True:
                global score
                score += 1
                print(f"Your score is : {score}")
                play_again()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Sorry, that's wrong. Final score: {score}")
                exit()

    play_again()


main()


