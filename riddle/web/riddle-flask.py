#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

import sys
import json

# App logic
# Get the riddle text
with open('riddle-text.json', 'r') as f:
  riddle = json.load(f)
  f.close()

def checkAnswer(ans):
  return

# Create webapp
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('./index.html')

@app.route("/query", methods = ['POST'])
def process_query():
  data = request.form
  print(data, file=sys.stderr)
  response = { 'msg' : 'Received: ' + data['solution'] }
  return json.dumps(response)

@app.route("/getriddle")
def send_riddles():
  args = request.args
  if "r" in args:
    return json.dumps(riddle)
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
