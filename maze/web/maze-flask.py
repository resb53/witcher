#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json

# Prepare maze details
with open('maze.json', 'r') as f:
  maze = json.load(f)

# Cardinal views
cardinals = ["n", "e", "s", "w"]

# base30
axes = ["a","b","c","d","e","f","g","h","i","j",
        "k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z","1","2","3","4"]

# Valid tiles
tiles = { "x" :"crossroads.jpg",
          "st":"straight-t.jpg",
          "lt":"left-t.jpg",
          "rt":"right-t.jpg",
          "s" :"straight.jpg",
          "lb":"left-b.jpg",
          "rb":"right-b.jpg",
          "oc":"orb-cyan.jpg",
          "or":"orb-red.jpg",
          "op":"orb-purple.jpg",
          "de":"dead-end.jpg" }

# Options for each tile
options = { "x" : ["w","d","s","a"],
            "st": ["d","s","a" ],
            "lt": ["w","s","a"],
            "rt": ["w","d","s"],
            "s" : ["w","s"],
            "lb": ["s","a"],
            "rb": ["d","s"],
            "oc": ["s"],
            "or": ["s"],
            "op": ["s"],
            "de": ["s"] }

movement = ["w","d","s","a"]

# Initialise
curDir = 0
curPos = "3k"

# Parse tile id
def setLoc(t):
  parts = list(t)
  global curDir
  curDir = cardinals.index(parts[2])
  global curPos
  curPos = ''.join([ parts[0], parts[1] ]) 

# Get colour from current grid position
def getColour(pos):
  [y, x] = breakdownLoc(pos)

  if 0 <= y <= 9:
    if 0 <= x <= 9:
      col = "a"
    elif 10 <= x <= 19:
      col = "b"
    elif 20 <= x <= 29:
      col = "c"
  elif 10 <= y <= 19:
    if 0 <= x <= 9:
      col = "d"
    elif 10 <= x <= 19:
      col = "e"
    elif 20 <= x <= 29:
      col = "f"
  elif 20 <= y <= 29:
    if 0 <= x <= 9:
      col = "g"
    elif 10 <= x <= 19:
      col = "h"
    elif 20 <= x <= 29:
      col = "i"

  return col

#Separate location into numeric values for each axes
def breakdownLoc(pos):
  yi = axes.index(pos[0])
  xi = axes.index(pos[1])
  return [yi, xi]

# Create webapp
app = Flask(__name__)

@app.route("/")
def index():
  args = request.args
  # Parse and check any specific tile request
  if "t" in args:
    setLoc(args["t"].lower())
  else:
    setLoc("3kn")

  loc = { "face": cardinals[curDir],
          "tile": curPos,
          "zone": getColour(curPos),
          "image": tiles[maze[cardinals[curDir]][curPos]] }

  return render_template('./index.html', loc=loc)

@app.route("/js/<path:path>")
def send_js(path):
  return send_from_directory('js', path)

@app.route("/css/<path:path>")
def send_css(path):
  return send_from_directory('css', path)

@app.route("/img/<path:path>")
def send_img(path):
  return send_from_directory('img', path)

# Maze specific web features
#@app.route("/gettile.jpg")
#def get_tile():
  # Calculate appropriate tile image and return it
#  image = "/".join([ getColour(curPos), tiles[maze[cardinals[curDir]][curPos]] ])
#  return send_from_directory('img', image)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(80))
