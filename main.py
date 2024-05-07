import random
import lilypond
import subprocess
from flask import Flask, render_template
from pattern_brain import Pattern_Brain

app = Flask(__name__)

brain = Pattern_Brain()
pattern = brain.gen_linear()

with open("file.ly", "w") as file:
  string = """\\version "2.25.12"
{
  c'4 e' g' b'
}
  """
  file.write(string)

subprocess.run([lilypond.executable(), "file.ly"])

@app.route('/')
def home():
  return render_template("./index.html")

if __name__ == "__main__":
  app.run(debug=True)

# create paramaters for etude creation

# when program is run, return a pattern

# make lilypond brain class to take pattern brain pattern and make lilypond pdf file

# display pdf file (music info)

