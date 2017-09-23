#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route("/")
def index():
  # If new player, give starting tile
  cur_tile = "n3kh"
  args = request.args

  # Parse and check the tile request
  if "t" in args:
    cur_tile = args["t"]
  loc = parse_tile(cur_tile)

  return render_template('./index.html', loc=loc)

@app.route("/gettile.jpg")
def get_tile():
  # Calculate appropriate tile image and return it
  image = "h/straight.jpg"

  return send_from_directory('img', image)

@app.route("/js/<path:path>")
def send_js(path):
  return send_from_directory('js', path)

@app.route("/css/<path:path>")
def send_css(path):
  return send_from_directory('css', path)

@app.route("/img/<path:path>")
def send_img(path):
  return send_from_directory('img', path)

def parse_tile(t):
  parts = list(t)
  loc = { "face": parts[0],
          "tile": ''.join([parts[1],parts[2]]),
          "zone": parts[3] }
  return loc

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(80))
