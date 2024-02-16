import random
from music21 import *

# create paramaters for etude creation

# when program is run, return a pattern

STICKINGS = ["R", "L", "K"]

new_pattern = []

pattern_length = 8
num = 0

def create_linear_pattern(notes):
  for i in range(notes):
    # check if last two notes in pattern are the same
    if len(new_pattern) >= 2 and new_pattern[-2] == new_pattern[-1]:
      values_to_choose = [val for val in STICKINGS if val != new_pattern[-1]]
      choice = random.choice(values_to_choose)
    else:
      choice = random.choice(STICKINGS)

    new_pattern.append(choice)

  print(new_pattern)

create_linear_pattern(pattern_length)

drumset = clef.PercussionClef()
m = stream.Measure([drumset])
m.show()