#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json

# App logic
commands = { '?': 'Shows the help text for a command.',
             'look': 'Looks around the area, listing objects of interest.',
             'use': 'Uses or interacts with an object that can be seen.',
             'back': 'Backs away form an object to take a wider look.' }

# Execute a valid command (checked in process_query)
def doCommand(com):
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
  elif com[0] == 'look':
    ret['msg'] = 'You look around.'
  elif com[0] == 'use':
    ret['msg'] = 'You use an object.'
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
