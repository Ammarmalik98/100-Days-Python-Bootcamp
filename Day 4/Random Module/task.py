import random
import my_module

#print(my_module.g_ratio)
#print(random.randint(1, 999))

coin_flips = int(random.randint(1, 10))

if coin_flips % 2 == 0:
    print("Heads")
else:
    print("Tails")