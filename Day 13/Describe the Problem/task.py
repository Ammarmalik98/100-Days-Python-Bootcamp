def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# The print statement isn't executed

# 1. What is the for loop doing?
# The for loop should iterate over the numbers 1 to 20

# 2. When is the function meant to print "You got it"?
# The function should print "You got it", when i == 20.

# 3. What are your assumptions about the value of i?
# The range function used does not include the second parameter and stops at n-1
# To solve this, we can make the second parameter 21 instead.