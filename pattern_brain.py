import random

class Pattern_Brain:
  def __init__(self):
    self.stickings = ["R", "L", "K"]
    self.length = 8
    self.pattern = []

  def gen_linear(self):
    for i in range(self.length):
      # check if last two notes in pattern are the same
      if len(self.pattern) >= 2 and self.pattern[-2] == self.pattern[-1]:
        val_to_choose = [val for val in self.stickings if val != self.pattern[-1]]
        choice = random.choice(val_to_choose)
      else:
        choice = random.choice(self.stickings)

      self.pattern.append(choice)

    print(self.pattern)
    return self.pattern