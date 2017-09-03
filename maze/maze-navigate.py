#!/usr/local/bin/python3

import sys
import json
import string

# Read maze object
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
          "de":"dead-end.jpg" };

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
            "de": ["s"] };

movement = ["w","d","s","a"]

#Navigate around the map - give infomation that would appear to the user
def main():
  # Initialise
  curDir = 0
  curPos = "3k"

  while curPos != "4j":
    print("You are looking " + cardinals[curDir] + " into square " + curPos);
    tile = maze[cardinals[curDir]][curPos]

    print("You see image " + getColour(curPos) + "/" + tiles[tile] + " and can choose to travel: " + str(options[tile]))

    travel = getUserAction(tile);

    [curDir, curPos] = navigate(travel, curDir, curPos)

#Get user movement and check move is valid on map
def getUserAction(tile):
  action = ""
  while action not in options[tile]:
    action = input("Enter next move:").lower()
    if action not in options[tile]:
      print("Invalid option.")
  return action

#Can assume valid move based on User Action Checks
def navigate(action, face, locn):
  #Breakdown location
  [yi, xi] = breakdownLoc(locn)

  #Calculate new attributes
  newFace = {
    "w": face,
    "d": (face + 1) % 4,
    "s": (face + 2) % 4,
    "a": (face + 3) % 4
  }[action]
  newLocn = calcNewSquare(yi, xi, newFace)

  return [newFace,newLocn]

#Separate location into numeric values for each axes
def breakdownLoc(pos):
  yi = axes.index(pos[0])
  xi = axes.index(pos[1])
  return [yi, xi]

#Calculate next square to present based on provided parameters
def calcNewSquare(yi, xi, dn):
  if dn == 0:
    yi -= 1
  elif dn == 1:
    xi += 1
  elif dn == 2:
    yi += 1
  elif dn == 3:
    xi -= 1
  return str(axes[yi]) + str(axes[xi])

#Retrieve correct coloured image
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

if __name__ == "__main__":
    main()
