# RANDOM MODULE: It is a built-in Python module used to generate random numbers and make random selections. 
# The random module generates pseudo-random numbers, meaning they appear random but are produced by an algorithm. For security-related tasks (passwords, tokens, cryptography), use the secrets module instead:

import random
#import my_module

#random_integer = random.randint(1, 10)
#print(random_integer)

#print(my_module.my_favorite_number)
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)


#random_float = random.uniform(1,10)
#print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
   print("Tails")

# when RUN this code it will print random number and random head or tail.