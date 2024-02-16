import random

# create paramaters for etude creation

# when program is run, return a pattern

STICKINGS = ["R", "L", "K"]

new_pattern = []

pattern_length = 8
num = 0

for i in range(pattern_length):
  # check if last two notes in pattern are the same
  if len(new_pattern) >= 2 and new_pattern[-2] == new_pattern[-1]:
    values_to_choose = [val for val in STICKINGS if val != new_pattern[-1]]
    choice = random.choice(values_to_choose)
  else:
    choice = random.choice(STICKINGS)

  new_pattern.append(choice)

print(new_pattern)