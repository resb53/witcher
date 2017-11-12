#!/usr/local/bin/python3

import sys
import json
import re
import codecs

# Get the riddle text
with open("riddle-text.json", "r") as f:
  riddle = json.load(f)
  f.close()

# Replace \n with <br>
for key in riddle:
  riddle[key] = riddle[key].split("\n")

# Modify clues

# Cyan, plaintext
riddle['cyantext'] = "<br>".join(riddle['cyantext'])

# Violet, reverse
puncspace = re.compile('([\.\,\;\:\!\?]) ')

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

riddle['violettext'] = "<br>".join(riddle['violettext'])

# red rot cipher
enc = codecs.getencoder( "rot-13" )
for i, s in enumerate(riddle['redtext']):
  riddle['redtext'][i] = enc( s )[0]

riddle['redtext'] = "<br>".join(riddle['redtext'])

# purple tr map
for i, s in enumerate(riddle['purpletext']):
  riddle['purpletext'][i] = s.translate(str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                                      'omktavgyezcjnbudxwfpirlshqOMKTAVGYEZCJNBUDXWFPIRLSHQ'))

riddle['purpletext'] = "<br>".join(riddle['purpletext'])

print(json.dumps(riddle, indent=2, separators=(',', ': ')))

