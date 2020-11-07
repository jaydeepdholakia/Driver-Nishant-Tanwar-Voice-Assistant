import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
#import wolframalpha
import json
import requests
import playsound
import random

print('Hello! I am a Personal Assistant of Rider OP. My name is Driver. Basically I am named after Rider, Driver. I hope you got the joke!')

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            exception_responses = ['thoda_uche_se_bolo.mp3','sunai_nahi_de_raha.mp3','firse_bol.mp3']
            playsound.playsound('Files/Hindi_Responses/'+random.choice(exception_responses), True)
            return "None"
        return statement

speak("Hello! I am a Personal Assistant of Rider OP. My name is Driver. Basically I am named after Rider, Driver. I hope you got the joke! Hahahaha")
wishMe()


if __name__=='__main__':

    while True:
        playsound.playsound('Files/Hindi_Responses/how_can_I_help_you.mp3',True)
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "bye" in statement or "stop" in statement:
            print('Do not forget to subscribe Rider OP!')
            playsound.playsound('Files/Hindi_Responses/bye.mp3', True)
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'tell a joke' in statement or 'tell me a joke' in statement:
            playsound.playsound('Files/Hindi_Responses/tell_a_joke_1.mp3', True)
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=KGb_wv-GIxs&list=PLqYhxkGfBhrX3jj6NkevYBcoD4mF33w6z")
            time.sleep(5)

        elif 'rider song' in statement or 'tik tok' in statement:
            playsound.playsound('Files/song/rider-provider-song.mp3', True)


        elif 'will i be on stream' in statement:
            playsound.playsound('Files/Hindi_Responses/will_I_be_on_stream.mp3', True)

        elif 'play among us' in statement:
            playsound.playsound('Files/Hindi_Responses/play_among_us.mp3', True)

        elif 'open google' in statement:
            playsound.playsound('Files/Hindi_Responses/ok.mp3', True)
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            playsound.playsound('Files/Hindi_Responses/ok.mp3', True)
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            playsound.playsound('Files/Hindi_Responses/ok.mp3', True)
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
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
            playsound.playsound('Files/Hindi_Responses/ok.mp3', True)
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Driver! version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, and gmail, tell time,get top headline news from times of india!'
                  'I also play Rider OP songs!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            playsound.playsound('Files/Hindi_Responses/who_made_you.mp3', True)
            print("JDOP has made me!")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search'  in statement:
            playsound.playsound('Files/Hindi_Responses/ok.mp3', True)
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif 'How many channel does Tanmay Bhat posses on Youtube' in statement:
            speak('Tanmay Bhat has namely 4 channel. Tanmay Bhat, Honestly by Tanmay Bhat, Samay Raina and Rider OP!')
            
        elif 'Why do you always speak the truth' in statement:
            speak('Speak I am always made to speak the truth by JDOP! Hope you are offended by the truth')


        else:
            #playsound.playsound('Files/Hindi_Responses/not_taught.mp3', True)
            playsound.playsound('Files/Hindi_Responses/iska superchat lagega.mp3', True)
            
        

time.sleep(3)
