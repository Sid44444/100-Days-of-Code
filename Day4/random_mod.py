import random
import my_module



random_integer=random.randint(2, 4)
print(random_integer)
print(my_module.my_favourite_number)

random_number_0_to_1 = random.random() * 10 #semi-open range, use this one if possible
print(random_number_0_to_1)

random_float= random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")