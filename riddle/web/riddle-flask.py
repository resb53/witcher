#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json
import re
import codecs

# App logic
answers = { '#cyantab':   { 'solution': 'fire',
                            'code': 0b1000 },
            '#violettab': { 'solution': 'banana',
                            'code': 0b0100 },
            '#purpletab': { 'solution': 'salt',
                            'code': 0b0010 }, 
            '#redtab':    { 'solution': 'bridge',
                            'code': 0b0001 } }
lstat = 0b0000
rstat = 0b0000

# Regex
puncspace = re.compile('([\.\,\;\:\!\?]) ')
articles = re.compile('^(the|an?) ')

# Get the riddle text
with open('riddle-text.json', 'r') as f:
  plainriddle = json.load(f)
  f.close()

# Modify riddle
def getRiddle(rstat):
  riddle = plainriddle.copy()

  # Replace \n with <br>
  for key in riddle:
    riddle[key] = riddle[key].split("\n")

  # Cyan, plaintext

  # Violet, reverse
  for i, s in enumerate(riddle['violettext']):
    # Decapitalise first
    s = s[:1].lower() + s[1:]
    # Move punc to the beginning
    s = s[-1:] + s[:-1]
    # Swap punc with spaces
    s = re.sub(puncspace, ' \g<1>', s)
    # Reverse the string
    s = s[::-1]
    # Capitalise new first
    riddle['violettext'][i] = s[:1].upper() + s[1:]

  # red rot cipher
  enc = codecs.getencoder( "rot-13" )
  for i, s in enumerate(riddle['redtext']):
    riddle['redtext'][i] = enc( s )[0]

  # purple tr map
  for i, s in enumerate(riddle['purpletext']):
    riddle['purpletext'][i] = s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                        'omktavgyezcjnbudxwfpirlshqOMKTAVGYEZCJNBUDXWFPIRLSHQ'))

  # Format for web viewing
  for key in riddle:
    riddle[key] = "<br><br>".join(riddle[key])

  return riddle

# Check answers
def checkAnswer(riddle,answer):
  global lstat
  # Compare lower case responses
  answer = answer.lower()
  # Remove articles if used
  answer = re.sub(articles, '', answer)
  # Compare and report
  if answer == answers[riddle]['solution']:
    lstat = lstat | answers[riddle]['code']
    return "That's right! " + answer[0].upper() + answer[1:] + " is correct. This will surely aid your allies. " + str(bin(lstat).count('0')) + " to go."
  else:
    return "I'm sorry, " + answer + " is not the answer I'm looking for. Please try again."

# Create webapp
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('./index.html')

@app.route("/query", methods = ['POST'])
def process_query():
  data = request.form
  print(data, file=sys.stderr)
  if 'riddle' in data and 'solution' in data:
    response = { 'msg' : "Skeleton> " + checkAnswer(data['riddle'], data['solution']) }
  else:
    respose = {'msg' : "Skeleton> I'm sorry there seems to have been a problem. Please inform the DM."}
  return json.dumps(response)

@app.route("/getriddle")
def send_riddles():
  args = request.args
  if "r" in args:
    return json.dumps(getRiddle(args['r']))
  else:
    return ("Invalid request", 400)

@app.route("/js/<path:path>")
def send_js(path):
  return send_from_directory('js', path)

@app.route("/css/<path:path>")
def send_css(path):
  return send_from_directory('css', path)

@app.route("/img/<path:path>")
def send_img(path):
  return send_from_directory('img', path)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(31332))
