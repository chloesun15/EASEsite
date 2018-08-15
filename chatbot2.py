from flask import Flask

app = Flask(__name__)

@app.route('/')

# --- Define your functions below! ---
def default():
    print("Sorry, I don't understand.")


def greeting():
    possible = ["Hi.", "Hello!","Hey.", "Salutations.", "Howdy!"]

    print (random.choice(possible))

def mood():
    possible = ["Good.", "Great!" "Bad", "Rough", "Let's not talk about me, shall we?", "Okay.", "Alright.", "So-so."]
    print (random.choice(possible))

def whatsup():
    possible = ["Not much.", "A lot.", "None of your business."]
    print (random.choice(possible))

def curses():
    print ("Don't be fucking rude.")

def question(keyword):
    affirmneg = ["Yes.", "No.", "Of course not.", "Of course.", "I'm afraid so.", "I'm afraid not.", "Definitely."]
    if keyword == ("?" or "do you" or "are you" or "am i" or "isn't"):
        print (random.choice(affirmneg))
    else:
        print ("I don't know.")
        joke()

def joke():
    jokes = ["What do chemists' dogs do with their bones?", "Why don't cats play poker in the jungle?", "Where do shellfish go to borrow money?", "What's the difference between a horse and the weather?"]
    punchline = ["They barium!", "There are too many cheetahs.", "The prawn broker.", "A horse is reigned up and the other rains down."]
    joke = input ("Would you like to hear a joke? Of course you do.")
    jokechoice = random.randint(0, len(jokes)-1)
    jokeresponse = input (jokes[jokechoice])
    print (punchline[jokechoice])

def process_input (response):
    cursesq = ["fuck you", "fuck u", "fuck", "shit", "cunt", "bitch", "whore", "hoe", "motherfucker", "fucker"]
    greetingq = ["hi","hewwo", "hello","hey", "bonjour", "hola", "salutations", "howdy"]
    moodq = ["how are you", "how's it going", "how is it going", "hows it going", "how do you feel"]
    whatsupq = ["what's up", "whats up", "whats going on", "que tal", "quetal"]
    questionq = ["where", "why", "how ", "who", "what", "do you", "are you", "?", "am i", "isn't"]
    master = [cursesq, greetingq, moodq, whatsupq, questionq]
    response = response.lower()
    respond = 0
    for i in master:
        if respond == 0:
            if i == cursesq:
                for i in cursesq:
                    if i in response:
                        respond = 1
                        curses()
                        break
            if i == greetingq:
                for i in greetingq:
                    if i in response:
                        respond = 1
                        greeting()
                        break
            if i == moodq:
                for i in moodq:
                    if i in response:
                        respond = 1
                        mood()
                        break
            if i == whatsupq:
                for i in whatsupq:
                    if i in response:
                        respond = 1
                        whatsup()
                        break
            if i == questionq:
                for i in questionq:
                    if i in response:
                        respond = 1
                        question(i)
                        break
    if respond == 0:
        if ("thank" or "ty") in response:
            print ("You're welcome.")
        elif ("bored") in response:
            joke()
        else:
            default()




# --- Put your main program below! ---
def main():
  import random
  greeting ()
  while True:
    answer = input("(What will you say?) ")
    process_input (answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
