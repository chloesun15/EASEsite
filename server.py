from flask import Flask, render_template
from flask import request
import json
import datetime
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/logout/', methods = ["GET", "POST"])
def logout():
  return render_template('home.html')

@app.route ('/link1/')
def link1():
    return render_template('register.html')

@app.route('/link2/')
def link2():
    return render_template('index.html')

@app.route ('/forgot/')
def forgot():
    return render_template('forgotpass.html')
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
    return render_template('home.html')

@app.route('/getsurvey/')
def getsurvey():
    return render_template('survey.html')

@app.route('/surveysubmit/', methods=["GET", "POST"])
def collectsurvey():
    q1 = request.form['text1']
    q2 = request.form['text2']
    q3 = request.form['text3']
    q4 = request.form['text4']
    answers = {}
    answers["q1"] = q1
    answers["q2"] = q2
    answers["q3"] = q3
    answers["q4"] = q4
    with open ("survey.json", "r") as readFile:
        dataList = json.load(readFile)
    dataList.append(answers)
    with open("survey.json", "w") as readFile:
        json.dump(dataList, readFile)
    return render_template('homepage.html')

@app.route('/forgotpass/', methods=["GET", "POST"])
def forgotpass():
    email1 = request.form['email']
    username1 = request.form['username']
    if (email1 == "") or (username1 == ""):
        return render_template('register.html', validity = 0)
    regInfo = {}
    regInfo["email"] = email1
    regInfo["username"] = username1
    with open("userinfo.json", "r") as readFile:
        dataList = json.load(readFile)
    for i in dataList:
        if (i["username"] == regInfo["username"]) and (i["email"] == regInfo["email"]):
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("easewebsitegwc@gmail.com", "EaseWeb246!")
            message = MIMEText("\n Hi " +i["name"] + "! \r\n Your password is " + i["password"])
            message['Subject'] = 'Ease Password Recovery'
            message['From'] = 'Ease'
            message['To'] = i["name"]
            s.sendmail("easewebsitegwc@gmail.com", i["email"], message.as_string())
            s.quit()
            return "Check your email!"
        else:
            return render_template('forgotpass.html', validity = 1)

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

@app.route('/mentalhealth/')
def mentalhealth():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('mentalhealth.html', username = username)
@app.route('/family/')
def family():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('familyissues.html', username = username)
@app.route('/random/')
def random():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('randomchat.html', username = username)
@app.route('/school/')
def school():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('schoolproblems.html', username = username)
@app.route('/relationship/')
def relationship():
    with open("currentuser.json", "r") as readFile:
        current = json.load(readFile)
    username = current[0]["user"]
    return render_template('relationshipproblems.html', username = username)


@app.route('/chat/')
def chat():
    return render_template('chat.html')

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
    diary = diary.replace("\r\n", "<br>")
    now = datetime.datetime.now()
    dot=now.strftime("%Y-%m-%d %H:%M")
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
    entry = entry.replace("\r\n", "<br>")
    now = datetime.datetime.now()
    dot=now.strftime("%Y-%m-%d %H:%M")
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
