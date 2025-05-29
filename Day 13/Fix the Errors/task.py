try:
    age = int(input("How old are you?\n"))
except ValueError:
    print("You didn't input a valid number, please input a numerical value e.g: 14")
    age = int(input("How old are you?\n"))

if age > 18:
    print(f"You can drive at age {age}.")
