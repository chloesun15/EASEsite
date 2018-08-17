from flask import Flask, render_template
from flask import request
import json
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/logout/')
def logout():
  return render_template('home.html')

@app.route ('/link1/')
def link1():
    return render_template('register.html')

@app.route('/link2/')
def link2():
    return render_template('index.html')

@app.route('/show/')
def show():
  with open("currentuser.json", "r") as readFile:
    current = json.load(readFile)
  username = current[0]["user"]
  with open("diary.json", "r") as readFile:
      dataList=json.load(readFile)
  AllEntries = []
  for i in dataList:
      AllEntries.append(i)
  return render_template('lastdiary.html', AllEntries = AllEntries, username = username)

@app.route('/register/', methods=["GET", "POST"])
def my_link():
    name1 = request.form['name']
    email1 = request.form['email']
    username1 = request.form['username']
    password1 = request.form['password']
    if (name1 == "") or (email1 == "") or (username1 == "") or (password1 == ""):
        return render_template('register.html', validity = 0)
    regInfo = {}
    regInfo["name"] = name1
    regInfo["email"] = email1
    regInfo["username"] = username1
    regInfo["password"] = password1
    with open("userinfo.json", "r") as readFile:
        dataList = json.load(readFile)
    for i in dataList:
        if i["username"] == regInfo["username"]:
            return render_template('register.html', validity = 1)
    dataList.append(regInfo)
    with open("userinfo.json", "w") as readFile:
        json.dump(dataList, readFile)
    return render_template('index.html')

@app.route('/login/', methods=["GET", "POST"])
def my_link2():
    user1 = request.form["username"]
    password1 = request.form["password"]
    with open("userinfo.json", "r") as readFile:
        dataList = json.load(readFile)
        readFile.close()
    with open("currentuser.json","r") as readFile:
        user= json.load(readFile)
        readFile.close()
    listlength = len(dataList)
    tries = 0
    for i in dataList:
        tries +=1
        if i["username"] == user1 and i["password"] == password1:
            user[0]["user"] = user1
            with open ("currentuser.json", "w") as readFile:
                json.dump(user, readFile)
            return render_template('homepage.html', username = user1)
        else:
            if tries == listlength:
                return render_template('home.html', validity = 0)
            else:
                continue

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/chat/')
def chat():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('chatwebsite.html', username = username)

@app.route('/diary/', methods=["GET", "POST"])
def diary():
    return render_template('diary.html')

@app.route('/forum/')
def forum():
    with open("forumposts.json","r") as readFile:
        allPosts = json.load(readFile)
    return render_template('forum.html', allPosts = allPosts)

@app.route('/resources/')
def resources():
    return render_template('resources.html')

@app.route('/return/')
def returnfx():
    return render_template('homepage.html')

@app.route('/back/')
def backfx():
    return render_template('home.html')

@app.route('/save/', methods=["GET", "POST"])
def save():
    entry={}
    diary = request.form['diary']
    now = datetime.datetime.now()
    dot=now.strftime("%Y-%M-%d %H:%M")
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    entry["date"]=dot
    entry["diary"] = diary
    entry["username"] = username
    with open("diary.json", "r") as readFile:
        dataList = json.load(readFile)
        dataList.append(entry)
        readFile.close()
    with open("diary.json", "w") as readFile:
        json.dump(dataList, readFile)
        readFile.close()
    return render_template('diary.html')


@app.route('/saveforum/', methods=["GET", "POST"])
def saveforum():
    userentry={}
    entry = request.form['entry']
    now = datetime.datetime.now()
    dot=now.strftime("%Y-%M-%d %H:%M")
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    userentry["date"]=dot
    userentry["entry"] = entry
    userentry["username"] = username
    with open("forumposts.json", "r") as readFile:
        diaryList = json.load(readFile)
        diaryList.append(userentry)
    with open("forumposts.json", "w") as readFile:
        json.dump(diaryList, readFile)
    with open("forumposts.json","r") as readFile:
        allPosts = json.load(readFile)
    return render_template('forum.html', allPosts = allPosts)

if __name__ == '__main__':
  app.run(debug=True)
