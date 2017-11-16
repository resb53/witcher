#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json
import requests

#         cvpr
lstat = 0b0000
rstat = 0b0000

# Prepare maze details
with open('maze.json', 'r') as f:
  maze = json.load(f)
  f.close()

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
          "od":"orb-done.jpg",
          "de":"dead-end.jpg",
          "ex":"exit.jpg",
          "md":"maze-done.jpg" }

# Options for each tile
options = { "x" : ["w","d","s","a"],
            "st": ["d","s","a" ],
            "lt": ["w","s","a"],
            "rt": ["w","d","s"],
            "s" : ["w","s"],
            "lb": ["s","a"],
            "rb": ["d","s"],
            "oc": ["s","action"],
            "or": ["s","action"],
            "op": ["s","action"],
            "od": ["s","noaction"],
            "de": ["s"],
            "ex": ["s","action"],
            "md": [] }

movement = ["w","d","s","a"]

# Orb status
act = { "oc": 1,
        "or": 1,
        "op": 1,
        "ex": 1 }

# Initialise
curDir = 0
curPos = "3k"

# Parse tile id
def setLoc(t):
  global curDir, curPos
  parts = list(t)
  curDir = cardinals.index(parts[2])
  curPos = "".join([ parts[0], parts[1] ]) 

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

# Separate location into numeric values for each axes
def breakdownLoc(pos):
  yi = axes.index(pos[0])
  xi = axes.index(pos[1])
  return [yi, xi]

# Prepare object to return to JS
def getLoc():
  tile = maze[cardinals[curDir]][curPos]
  # get pixels for minimap
  [top, left] = curPos
  top = int(axes.index(top) * 10 - 299)
  left = int(axes.index(left) * 10 - 145)
  return { "face": cardinals[curDir],
           "tile": curPos,
           "zone": getColour(curPos),
           "image": tiles[tile],
           "allowed": options[tile],
           "action": act,
           "left": left,
           "top": top,
           "rstat": bin(rstat).count('1') }

# Outwards comms
def sendrstat():
  if lstat & 8 == 8:
    c = requests.post("http://riddle.morphygames.co.uk/rstat", data={'rstat': 0b1000} )
  if lstat & 4 == 4:
    #v = requests.post("http://maze.morphygames.co.uk/rstat", data={'rstat': 0b0100} )
  if lstat & 2 == 2:
    p = requests.post("http://escape.morphygames.co.uk/rstat", data={'rstat': 0b0010} )
  if lstat & 1 == 1:
    print("!!!RED ACHIEVED!!!", file=sys.stderr)

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

  return render_template('./index.html', loc=getLoc())

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
@app.route("/navigate")
def navigate():
  global curDir, curPos
  args = request.args
  if "a" in args:
    # Get current attributes
    [yi, xi] = breakdownLoc(curPos)
    # Calculate new direction
    curDir = {
      "w": curDir,
      "d": (curDir + 1) %4,
      "s": (curDir + 2) %4,
      "a": (curDir + 3) %4
    }[args["a"]]
    # Calculate new position
    if curDir == 0:
      yi -= 1
    elif curDir == 1:
      xi += 1
    elif curDir == 2:
      yi += 1
    elif curDir == 3:
      xi -= 1
    curPos = "".join([axes[yi], axes[xi]])

    return json.dumps(getLoc(), separators=(',',':'))

@app.route("/doaction")
def doAction():
  global act, maze, lstat
  args = request.args
  print(args, file=sys.stderr)
  if "t" in args:
    # Try to do the action
    tile = maze[cardinals[curDir]][curPos]
    if act[tile]:
      if tile == "ex":
        maze[cardinals[curDir]][curPos] = "md"
        lstat |= 0b0100
      else:
        maze[cardinals[curDir]][curPos] = "od"
        if args['t'] == 'dyn':
          lstat |= 0b0001
        elif args['t'] == 'dde':
          lstat |= 0b0010
        elif args['t'] == 'nne':
          lstat |= 0b1000
      sendrstat()
      act[tile] = 0

    return json.dumps(getLoc(), separators=(',',':'))

@app.route("/reset")
def reset():
  global maze, curDir, curPos, act
  # Reset Maze
  with open('maze.json', 'r') as f:
    maze = json.load(f)
    f.close()
  # Reset Start
  curDir = 0
  curPos = "3k"
  # Reset Actions
  act = { "oc": 1,
          "or": 1,
          "op": 1,
          "ex": 1 }
  lstat = 0b0000
  
  return ('Maze Reset Successfully.', 200)

@app.route("/rstat", methods = ['POST'])
def updateStat():
  global rstat
  data = request.form
  print(data, file=sys.stderr)
  if 'rstat' in data:
    rstat |= int(data['rstat'])
    return ('rstat successful', 200)
  else:
    return ('rstat form corrupted.', 400)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(31331))
