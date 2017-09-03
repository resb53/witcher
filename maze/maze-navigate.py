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

def main():
  # Initialise
  curDir = 0
  curPos = "3k"

  while curPos != "4j":
    print("You are looking " + cardinals[curDir] + " into square " + curPos);
    tile = maze[cardinals[curDir]][curPos]

    print("You see image " + tiles[tile] + " and can choose to travel: " + str(options[tile]))

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
  [y, x] = [locn[0], locn[1]]
  yi = axes.index(y)
  xi = axes.index(x)

  #Calculate new attributes
  if action == "w":
    #Move forwards a square in the direction faced, don't change direction.
    newFace = face

  elif action == "d":
    #Turn facing clockwise 1 cardinal point, and move a square in that direction
    newFace = (face + 1) % 4

  elif action == "s":
    #Reverse facing, and move view a tile backwards
    newFace = (face + 2) % 4

  elif action == "a":
    #Turn facing anticlockwise 1 cardinal point, and move a square in that direction
    newFace = (face - 1) % 4

  newLocn = calcNewSquare(yi, xi, newFace)
  return [newFace,newLocn]

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

if __name__ == "__main__":
    main()
