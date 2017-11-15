#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json

# App logic
commands = { '?': 'Shows the help text for a command.',
             'focus': 'Specifies what item you are currently focusing on.',
             'look': 'Looks around the area, listing objects of interest.',
             'use': 'Uses or interacts with the current focused object, or shifts focus to a new specified object that can be seen.',
             'take': 'Attempt to take an item and collect it in your inventory.',
             'combine': 'Attempt to combine the item currently in focus with a named item in your inventory. Used alone will list your inventory.',
             'solve': 'Use with a solution word or number to solve the current focused item\'s puzzle.',
             'inv': 'Focus on your inventory insteam of the room.',
             'back': 'Backs away from an object or your inventory to take a wider look.' }

# Something about current level, to vary between looking around the room and in more detail. A counter?
# A global to hold the current item of focus? Use 'room' for this and as the base root?
# OOP. ish. Have a load of JSON object wiht parameters that affect how the base commands handle them.
level = 'room'

# Get the riddle text
with open('escape-room.json', 'r') as f:
  theroom = json.load(f)
  f.close()

# Only allow changing the current level after checking it exists
def setLevel(l):
  global level
  if l in theroom:
    level = l
    return 'You now focus on the ' + level + '.'
  else:
    return 'Error: ' + l + ' is missing from theroom. Inform the DM.'

# Execute a valid command (checked in process_query)
def doCommand(com):
  global theroom
  ret = { 'msg': 'default response' }
  # Process per command
  # List available commands
  if com[0] == '?':
    if len(com) == 1:
      ret['msg'] = ' &emsp; '.join(commands.keys())
    elif len(com) == 2:
      if com[1] in commands:
        ret['msg'] = com[1] + ': ' + commands[com[1]]
      else:
        ret['msg'] = 'Error: command not recognised. Use ? to list available commands, and ? followed by a command for more info.'
    else:
      ret['msg'] = 'Too many arguments. ? can only be used with up to one additional command.'
  # Report the current focus level
  elif com[0] == 'focus':
    ret['msg'] = 'You currently focus on the ' + level + '.'
  # Look at the current level. No additional commands.
  elif com[0] == 'look':
    if len(com) == 1:
      # Check if there are multiple states
      if 'status' not in theroom[level]:
        ret['msg'] = theroom[level]['description']
      else:
        ret['msg'] = theroom[level]['description'][theroom[level]['status']]
      if len(theroom[level]['children']) > 0:
        ret['msg'] = ret['msg'] + ' It contains: ' + ', '.join(theroom[level]['children'])
    else:
      ret['msg'] = 'Error: You cannot look at an item. Use it first to approach and then look.'
  # Use the current level. Or a specified item within.
  elif com[0] == 'use':
    if len(com) == 1:
      if len(theroom[level]['onuse']) > 0:
        ret['msg'] = theroom[level]['onuse'][0]['description']
        if 'next' in theroom[level]['onuse'][0]:
          # If only one item, focus on it and handle it
          if len(theroom[level]['onuse'][0]['next']) == 1:
            # See if we can focus on the new item
            oldlevel = level
            setmsg = setLevel(theroom[level]['onuse'][0]['next'][0])
            # If successful, add the new item to its parents index, and remove the onuse effect from its parent
            if setmsg[:5] != 'Error':
              ret['msg'] = ret['msg'] + ' ' + setmsg
              theroom[theroom[level]['parent']]['children'].append(level)
              theroom[oldlevel]['onuse'].pop(0)
            else:
              ret['msg'] = setmsg
          # If more than one item, just return use description and add all items to their parents, removing this onuse effect.
          else:
            for item in theroom[level]['onuse'][0]['next']:
              if item in theroom:
                theroom[theroom[item]['parent']]['children'].append(item)
              else:
                ret['msg'] = ret['msg'] + ' Error: ' + item + ' is missing from theroom. Inform the DM.'
            theroom[level]['onuse'].pop(0)
      else:
        ret['msg'] = 'You do not know what to do with the ' + level + '.'
    # Approach an object that can be seen
    elif len(com) == 2:
      if com[1] in theroom[level]['children']:
        ret['msg'] = 'You focus on the ' + com[1] + '.'
        if com[1] in theroom:
          ret['msg'] = setLevel(com[1])
        else:
          ret['msg'] = 'Error: This item is visible, but missing from theroom. Inform the DM.'
      else:
        ret['msg'] = 'You cannot see a ' + com[1] + '.'
    else:
      ret['msg'] = 'Error: You can attempt to use the current item, or an item within it, specifying the item second. You cannot use more than one at once.'
  # Take the current level.
  elif com[0] == 'take':
    if len(com) == 1:
      if level == 'inventory':
        ret['msg'] = 'You\'ve already gathered everything in your inventory.'
      elif theroom[level]['size'] == 'small':
        oldparent = theroom[level]['parent']
        # Remove the item from its parent and add it to the inventory
        theroom[oldparent]['children'].remove(level)
        theroom['inventory']['children'].append(level)
        theroom[level]['parent'] = 'inventory'
        # Return to the old parent
        ret['msg'] = 'You take the ' + level + ' and place it in your inventory. ' + setLevel(oldparent)
      else:
        ret['msg'] = 'You are unable to take the ' + level + '. It is too ' + theroom[level]['size'] + '.'
    else:
       ret['msg'] = 'Error: You can only take the item currently being observed. Use it first to approach and then take.'
  # Combine an inventory item with the current focus.
  elif com[0] == 'combine':
    if len(com) == 1:
      ret['msg'] = 'Inventory: ' + ', '.join(theroom['inventory']['children'])
    if len(com) == 2:
      # See if this is a valid item in the inventory
      if com[1] in theroom['inventory']['children']:
        # See if the current focus has a combination with this specified item.
        if 'combine' in theroom[level] and com[1] in theroom[level]['combine']:
          ret['msg'] = theroom[level]['combine'][com[1]]['description']
          # See if anything else happens
          if 'next' in theroom[level]['combine'][com[1]]:
            # See if we can focus on the new item
            oldlevel = level
            setmsg = setLevel(theroom[level]['combine'][com[1]]['next'])
            # If successful, add the new item to its parents index, and remove the onuse effect from its parent
            if setmsg[:5] != 'Error':
              ret['msg'] = ret['msg'] + ' ' + setmsg
              theroom[theroom[level]['parent']]['children'].append(level)
              # Delete previous items if that is intended
              if theroom[oldlevel]['combine'][com[1]]['destroy']:
                theroom.pop(oldlevel)
                theroom.pop(com[1])
            else:
              ret['msg'] = setmsg
        else:
          ret['msg'] = 'You don\'t know how to combine the ' + com[1] + ' with the ' + level + '.'
      else:
        ret['msg'] = 'Error: Cannot find the ' + com[1] + ' in your inventory.'
  # Attempt to solve a puzzle.
  elif com[0] == 'solve':
    if 'solve' in theroom[level]:
      if len(com) == 2:
        # Check the solution
        if theroom[level]['solve']['solution'] == com[1]:
          ret['msg'] = theroom[level]['solve']['description']
          # Update the object to reflect changes
          for key in theroom[level]['solve']['update'].keys():
            theroom[level][key] = theroom[level]['solve']['update'][key]
        else:
          ret['msg'] = 'That solution doesn\'t seem to solve the puzzle.'
      else:
        ret['msg'] = 'Error: You must supply a single solution with this command.'
    else:
      ret['msg'] = 'You don\'t know how to solve the ' + level + '.'
  # Look at your inventory
  elif com[0] == 'inv':
    if len(com) == 1:
      ret['msg'] = 'You inspect your inventory.'
      theroom['inventory']['parent'] = level
      setLevel('inventory')
    else:
      ret['msg'] = 'Error: \'inv\' must be used as a single command.'
  # Back away to the previous level
  elif com[0] == 'back':
    if len(com) == 1:
      if 'parent' in theroom[level]:
        ret['msg'] = 'You back away from the ' + level + '. ' + setLevel(theroom[level]['parent'])
      else:
        ret['msg'] = 'You cannot back away any further.'
    else:
      ret['msg'] = 'Error: \'back\' must be used as a single command.'
  return ret

# Create webapp
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('./index.html')

@app.route("/query", methods = ['POST'])
def process_query():
  data = request.form
  print(data, file=sys.stderr)
  if 'command' in data:
    command = data['command'].lower()
    comlist = command.split(' ')
    if comlist[0] in commands:
      response = doCommand(comlist)
    else:
      response = { 'msg' : 'Error: command not recognised. Use ? to list available commands, and ? followed by a command for more info.' }
  else:
    response = { 'msg' : "There seems to have been a problem. Please inform the DM." }
  return json.dumps(response)

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
  app.run(host="0.0.0.0", port=int(31333))
