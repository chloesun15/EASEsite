from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/', methods=["GET", "POST"])
def my_link():
  tag = request.form['expression']
  with open("userinfo.json", "r") as readFile:
      dataList = json.load(readFile)
      dataList.append(tag)
      readFile.close()
  with open("userinfo.json", "w") as readFile:
      json.dump(dataList, readFile)

if __name__ == '__main__':
  app.run(debug=True)
