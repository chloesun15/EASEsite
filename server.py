from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)

@app.route ('/link1/')
def link1():
    return render_template ('register.html')

@app.route('/link2/')
def link2():
    return render_template('index.html')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/my-link/', methods=["GET", "POST"])
def my_link():
    name1 = request.form['name']
    email1 = request.form['email']
    username1 = request.form['username']
    password1 = request.form['password']
    regInfo = {}
    regInfo["name"] = name1
    regInfo["email"] = email1
    regInfo["username"] = username1
    regInfo["password"] = password1
    with open("userinfo.json", "r") as readFile:
        dataList = json.load(readFile)
        dataList.append(regInfo)
        readFile.close()
    with open("userinfo.json", "w") as readFile:
        json.dump(dataList, readFile)
    return render_template('index.html')

@app.route('/my-link2/', methods=["GET", "POST"])
def my_link2():
    user1 = request.form["username"]
    password1 = request.form["password"]
    with open("userinfo.json", "r") as readFile:
        dataList = json.load(readFile)
        readFile.close()
    listlength = len(dataList)
    tries = 0
    for i in dataList:
        tries +=1
        if i["username"] == user1 and i["password"] == password1:
                return render_template('homepage.html')
        else:
            if tries == listlength:
                return 'unsuccessful'
            else:
                continue

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/chat/')
def chat():
    return render_template('chat.html')

@app.route('/diary/')
def diary():
    return render_template('diary.html')
    
@app.route('/forum/')
def forum():
    return render_template('forum.html')

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/return/')
def returnfx():
    return render_template('homepage.html')

if __name__ == '__main__':
  app.run(debug=True)
