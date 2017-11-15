#!/usr/local/bin/python3

import sys
import json

with open(sys.argv[1], 'r') as f:
  theroom = json.load(f)
  f.close()

print("No errors.")
