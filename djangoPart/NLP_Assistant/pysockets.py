import asyncio
import websockets
import json
import speech_recognition as sr
#############################
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
# from ecapture import ecapture as ec
import wolframalpha
import requests
from googlesearch import search

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate',180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def gSearch(statement):
    query = statement.replace('search for', '')
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab(
            "https://google.com/search?q=%s" % query
        )
    speak('these are some results')
    return 'check the tab'

def driver(statement):
    # speak("ok all set")
    if "goodbye" in statement or "ok bye" in statement or "stop" in statement:
        speak('okay i am right here if you need me, Good bye')
        return 'okay i am right here if you need me, Good bye'

    if 'search wiki for' in statement:
        speak('Searching Wikipedia...')
        statement =statement.replace("search wikipedia for ", "")
        print(statement)
        results = wikipedia.summary(statement, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return results

    elif 'search for' in statement:
        gSearch(statement)
        return None

    elif 'open youtube' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        return None

    elif 'open google' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        return None

    elif 'open gmail' in statement:
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new_tab("gmail.com")
        speak("Google Mail open now")
        return None

    elif "weather" in statement:
        api_key="8ef61edcf1c576d65d836254e11ea420"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        if len(statement.split())<2:
            return 'enter weather __cityName__'
        city_name=statement.split()[1]
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
            return (" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        else:
            speak(" City Not Found ")
            return' City Not Found '

    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
        return f"the time is {strTime}"

    elif 'who are you' in statement or 'what can you do' in statement or "state yourself" in statement:
        speak('I am Cross version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube, gmail and stackoverflow ,predict time,take a photo,search google,wikipedia,predict weather' 
              'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
        return ('I am Cross version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube, gmail and stackoverflow ,predict time,take a photo,search google,wikipedia,predict weather' 
              'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("Here is stackoverflow")
        return None

    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        return 'Here are some headlines from the Times of India,Happy reading'

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
        return 'its '+answer

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("i am created by some engineers at DAVIET")
        return "i am created by some engineers at DAVIET"










async def chat_receiver(websocket, path):
    async for message in websocket:
        message = json.loads(message)
        text = message['text']
        chat_response = driver(text)
        print(chat_response)
        await websocket.send(json.dumps({'response': chat_response}))

async def router(websocket, path):
	if path == "/":
		await chat_receiver(websocket, path)

    #the code below is how you add other path's
    
	# elif path == "/shade-area":
	# 	await get_shaded_area(websocket, path)
	# elif path == '/render':
	# 	await render(websocket, path)

asyncio.get_event_loop().run_until_complete(websockets.serve(router, '0.0.0.0', 8765))

asyncio.get_event_loop().run_forever()