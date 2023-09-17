import random
import string
random.seed(10)
letters = string.ascii_lowercase
rand_letters = random.choices(letters,k=5) # where k is the number of required rand_letters

print(rand_letters)

['o', 'l', 'p', 'f', 'v']
