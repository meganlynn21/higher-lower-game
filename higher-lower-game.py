from art import logo
from art import vs
from game_data import data
import random

choice1 = data
choice2 = data


# Retrieve random values from game_data dictionary for guess 1 and guess 2
def guess1(one):
    one = random.choice(data)
    return one


def guess2(two):
    two = random.choice(data)
    return two


"""Compare the amount of followers from the list of dictionaries and 
take string input as first choice A or second choice B"""


def compare(string):
    if string == "A" and first_choice['follower_count'] > second_choice['follower_count']:
        print(f"A is greater {first_choice['follower_count']} {second_choice['follower_count']}")
        return "Your right!"
    if string == "A" and first_choice['follower_count'] < second_choice['follower_count']:
        print(f"B is greater {first_choice['follower_count']} {second_choice['follower_count']}")
        return "You Lose!"

    if string == "B" and first_choice['follower_count'] < second_choice['follower_count']:
        print(f"B is greater {first_choice['follower_count']} {second_choice['follower_count']}")
        return "Your Right!"
    if string == "B" and first_choice['follower_count'] > second_choice['follower_count']:
        print(f"A is greater {first_choice['follower_count']} {second_choice['follower_count']}")
        return "You Lose!"
    else:
        print(f"neither is right {first_choice['follower_count']} {second_choice['follower_count']}")
        return "no"


# If user selects correct input then print this above "You're right! Current score: (put score here)" the first compare

# Create a count variable to hold the score and create a loop to keep the game going

first_choice = guess1(choice1)
second_choice = guess2(choice2)

print(logo)
print("Which of the following has more followers or are same?")
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
print(vs)
print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
a_or_b = input("Who has more followers? Type 'A' or 'B': ")

print(compare(a_or_b))