#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('./index.html')

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
  app.run(host="0.0.0.0", port=int(80))
