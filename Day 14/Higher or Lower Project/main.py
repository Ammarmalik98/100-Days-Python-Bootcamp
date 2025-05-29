import game_data
import art
source = game_data.data
position = 0
score = 0

def team_A():
    print(art.logo)
    print(f"Compare A: {source[position]["name"]}, a {source[position]["description"]}, from {source[position]["country"]} ")


def team_B():
    print(art.vs)
    print(f"Against B: {source[position + 1]["name"]}, a {source[position+1]["description"]}, from {source[position+1]["country"]} ")

team_A()
team_B()

guess = input("Who has more followers? A or B").upper()

team_A_followers = source[position]["follower_count"]
team_B_followers = source[position + 1]["follower_count"]

if guess == "A":
    if team_A_followers > team_B_followers:
        score += 1
        print("You are correct!")
    else:
        print("You are incorrect!")
elif guess == "B":
    if team_A_followers < team_B_followers:
        score += 1
        print("You are correct!")
    else:
        print("You are incorrect!")
print(score)