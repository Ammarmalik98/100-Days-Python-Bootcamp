# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"How is the weather over at {location}?")
#
# greet_with("Ammar", "London")

# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"How is the weather over at {location}?")
#
# greet_with(location ="London", name="Ammar Malik")

true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]




def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    true_container = []
    for letter in true:
        if letter in name1:
            score1 += 1
            if letter in name2:
                score2 += 1
    for letter in love:
        if letter in name1:
            score1 += 1
            if letter in name2:
                score2 += 1
    print(f"{score1}{score2}")


calculate_love_score("klein morreti", "audrey hall")