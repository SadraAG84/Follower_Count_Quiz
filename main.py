from Art import logo
from Art import vs
from Game_data import data
import random

print(logo)

# Getting a random account


def random_acc():
    global rand_data
    rand_data = random.choice(data)
    return rand_data

# Formatting random account


def formatting(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} which is {description} from {country}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return "a"
    else:
        return "b"


def game():
    score = 0
    should_continue = True
    while should_continue:
        account_a = random_acc()
        account_b = random_acc()

        while account_a == account_b:
            account_b = random_acc()

        a_follower = int(account_a["follower_count"])
        b_follower = int(account_b["follower_count"])

        account_a = formatting(account_a)
        account_b = formatting(account_b)

        print(f"\nA= {account_a} {vs}\n  B= {account_b}\n")
        guess = input("Which has more follower  'A' or 'B'?  ").lower()

        is_correct = check_answer(guess, a_follower, b_follower)

        if guess == is_correct:
            score += 1
            print(f"Thats true your score is {score}")
        else:
            print(f"Your answer is fasle and your last score is {score}")
            should_continue = False


game()
