from art import logo
from art import vs
from game_data import data
import random
import os

score = 0


def main():
    # Retrieve random values from game_data dictionary
    first_choice = random.choice(data)
    second_choice = random.choice(data)
    # The two choices cannot be the same
    if first_choice == second_choice:
        return main()
    print(logo)
    print("Which of the following has more followers?")
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
    a_or_b = input("Who has more followers? Type 'A' or 'B': ")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Compare the amount of followers from the list of dictionaries and
    # take string input as first choice A or second choice B
    def compare(string):
        a_choice = "A"
        b_choice = "B"
        if string == a_choice and first_choice['follower_count'] > second_choice['follower_count']:
            print(f"A is greater {first_choice['follower_count']} {second_choice['follower_count']}")
            print("Your Right!")
            return True
        elif string == a_choice and first_choice['follower_count'] < second_choice['follower_count']:
            print(f"B is greater {first_choice['follower_count']} {second_choice['follower_count']}")
            return False
        elif string == b_choice and first_choice['follower_count'] < second_choice['follower_count']:
            print(f"B is greater {first_choice['follower_count']} {second_choice['follower_count']}")
            print("Your Right!")
            return True
        elif string == b_choice and first_choice['follower_count'] > second_choice['follower_count']:
            print(f"A is greater {first_choice['follower_count']} {second_choice['follower_count']}")
            return False
        else:
            main()

    # Create a count variable to hold the score and create a loop to keep the game going

    while compare(a_or_b):
        global score
        score += 1
        print(f"Your score is : {score}")
        main()
    else:
        print("YOU LOSE")


main()
