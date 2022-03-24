import random
from game_data import data

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

def account_perimeters(account1, account2):
    global account_name_a
    global follower_count_a
    global account_description_a
    global country_a

    global account_name_b
    global follower_count_b
    global account_description_b
    global country_b

    account_name_a = account1["name"]
    follower_count_a = account1["follower_count"]
    account_description_a = account1["description"]
    country_a = account1["country"]

    account_name_b = account2["name"]
    follower_count_b = account2["follower_count"]
    account_description_b = account2["description"]
    country_b = account2["country"]

already_shown = []
score = 0
win = True

def account_strings():
    global account_a_string
    global account_b_string

    account_a_string = f"Compare A: {account_name_a}, a {account_description_a}, from {country_a}."
    account_b_string = f"Against B: {account_name_b}, a {account_description_b}, from {country_b}."
    print(account_a_string + "\n" + account_b_string)
    # print(f"Compare A: {account_name_a}, a {account_description_a}, from {country_a}.")
    # print(f"Against B: {account_name_b}, a {account_description_b}, from {country_b}.")

# def add_already_shown():
#     if account_name_a not in already_shown:
#         already_shown.append(account_a)
#     if account_name_b not in already_shown:
#         already_shown.append(account_b)

account_perimeters(account_a, account_b)
print(" ")
print(f"Compare A: {account_name_a}, a {account_description_a}, from {country_a}.")
print(f"Against B: {account_name_b}, a {account_description_b}, from {country_b}.")
# account_strings()
guess = input("Who do you think has the most followers on Instagram? Type either A or B. ")

while win:
    print(f"\n{account_name_a} has {follower_count_a} followers, and {account_name_b} has {follower_count_b} followers.")
    if (follower_count_a > follower_count_b):
        if guess == "a":
            print("You Win!\n")
            score += 1
            already_shown.append(account_a)
            already_shown.append(account_b)
        else:
            print("You Lose!")
            win = False
            break
    else:
        if guess == "b":
            print("You Win!\n")
            score += 1
            already_shown.append(account_a)
            already_shown.append(account_b)
            account_a = account_b
            
        else:
            print("You Lose!")
            win = False
            break
    
    account_b = random.choice(data)
    while account_b in already_shown:
        account_b = random.choice(data)
    
    # print(already_shown)
    account_perimeters(account_a, account_b)
    account_strings()
    
    if len(data) == 0:
        print("You've won the game!!!")
        break
    guess = input("Who do you think has the most followers on Instagram? Type either A or B. ")

print(f"Final Score: {score}")