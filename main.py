import random
import lilypond
import subprocess
from pattern_brain import Pattern_Brain

brain = Pattern_Brain()
pattern = brain.gen_linear()

with open("files.ly", "w") as file:
  string = """\\version "2.25.12"
{
  c'4 e' g' b'
}
  """
  file.write(string)

subprocess.run([lilypond.executable(), "files.ly"])

# create paramaters for etude creation

# when program is run, return a pattern

# make lilypond brain class to take pattern brain pattern and make lilypond pdf file

# display pdf file (music info)

