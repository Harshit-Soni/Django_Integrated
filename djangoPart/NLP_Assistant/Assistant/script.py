import speech_recognition as sr
import pyttsx3
import datetime
print('Cross Loading...')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate',180)
print('evrything loaded')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Boss")
        print("Hello,Good Morning")
    elif hour>=12 and hour<14:
        speak("Hello,Good Afternoon Boss")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening Boss")
        print("Hello,Good Evening")

greet()
speak('''I am Cross version 1 point O your personal assistant. I am programmed to minor tasks like
        searching web,wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!''')
speak("i am created by some engineers at DAVIET")