#!/usr/local/bin/python3

import sys
import requests

allowed = ['cyan','violet','purple']

# Outwards comms
def sendrstat(colour):
  if colour == 'cyan':
    c = requests.post("http://riddle.morphygames.co.uk/rstat", data={'rstat': 0b0001} )
  elif colour == 'violet':
    v = requests.post("http://maze.morphygames.co.uk/rstat", data={'rstat': 0b0001} )
  elif colour == 'purple':
    p = requests.post("http://escape.morphygames.co.uk/rstat", data={'rstat': 0b0001} )

if __name__ == "__main__":
  if sys.argv[1] in allowed:
    sendrstat(sys.argv[1])
  else:
    print('Error: Please supply a valid colour.', file=sys.stderr)
