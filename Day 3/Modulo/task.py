user_input = int(input("Please input a 2-digit number: \n"))

opp = user_input % 2
if opp > 0:
    print(f"{user_input} is an odd number")
else:
    print(f"{user_input} is an even number")