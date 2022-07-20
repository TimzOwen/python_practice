# Rock paper and scissor Game:

import sys

user_name1 = input("Hello, What your name? ")
user_name2 = input("And you? ")
user_1 = input(f"Hey {user_name1}, Do you want to choose rock, scissor or paper?...")
user_2 = input(f"what about you {user_name2}, what do you choose?...")

def compare_game(u1, u2):
    if u1 == u2:
        return " Its a tie for you two"
    elif(u1 == "rock"):
        if (u2 == "scissor"):
            return "Rock wins !!"
        else:
            return "Paper wins !!"
    elif (u1 == "scissor"):
        if(u2 == "paper"):
            return "Scissor wins !!"
        else:
            return "Rock wins !!"
    elif (u1 == "paper"):
        if(u2== "rock"):
            return "Paper wins !!"
        else:
            return "Scissor wins !!"
    else:
        return "Try again, you did not select either Rock, Scissor or Paper"
        sys.exit()

print(compare_game(user_1,user_2))