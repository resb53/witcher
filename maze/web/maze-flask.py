#!/usr/local/bin/python3

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('./index.html')

@app.route("/js/<path:path>")
def send_js(path):
  return send_from_directory('js', path)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(80))
