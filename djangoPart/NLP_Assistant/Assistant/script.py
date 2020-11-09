import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
# from ecapture import ecapture as ec
import wolframalpha
import requests
from googlesearch import search

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

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source, duration=3)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
def gSearch(statement):
    query = statement.replace('search for', '')
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(
            "https://google.com/search?q=%s" % query
        )
    speak('these are some results')
    time.sleep(5)


speak("hey its your virtual assistant Cross wait for me to load all modules")
# speak("ok all set")
greet()
print('starting now')
while True:
    speak("Tell me how can I help you now?")
    statement = listen().lower()
    if statement==0:
        continue

    if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
        speak('okay i am right here if you need me, Good bye')
        print('okay i am right here if you need me, Good bye')
        break

    if 'search wikipedia for' in statement:
        speak('Searching Wikipedia...')
        statement =statement.replace("search wikipedia for ", "")
        print(statement)
        results = wikipedia.summary(statement, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'search for' in statement:
        gSearch(statement)

    elif 'open youtube' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)

    elif "weather" in statement:
        api_key="8ef61edcf1c576d65d836254e11ea420"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name=listen()
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))
            print(" Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))
        else:
            speak(" City Not Found ")

    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'who are you' in statement or 'what can you do' in statement or "state yourself" in statement:
        speak('I am Cross version 1 point O your personal assistant. I am programmed to minor tasks like'
                'opening youtube, gmail and stackoverflow ,predict time,take a photo,search google,wikipedia,predict weather' 
                'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")

    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    # elif "camera" in statement or "take a photo" in statement:
    #     ec.capture(0,"robo camera","img.jpg")

    elif 'what is ' in statement:
        # speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question=statement
        client = wolframalpha.Client('45A66P-H9T8PKQGU8')

        try:
            res = client.query(question)
            answer = next(res.results).text
        except:
            answer=''
            gSearch(statement)
        speak('its '+answer)
        print(answer)

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("i am created by some engineers at DAVIET")


    # elif "log off" in statement or "sign out" in statement:
    #     speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    #     subprocess.call(["shutdown", "/l"])

time.sleep(3)
