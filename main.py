import random

# create paramaters for etude creation

# when program is run, return a pattern

STICKINGS = ["R", "L", "K"]

new_pattern = []

pattern_length = 8
num = 0

for i in range(pattern_length):
  choice = random.choice(STICKINGS)
  new_pattern.append(choice)

print(new_pattern)