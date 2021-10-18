import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia,webbrowser
import os
import smtplib
import sys
from googlesearch import search
import pywhatkit as pwt

from wikipedia.wikipedia import search              #program by Aftab Mallick
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning!")
    elif hour >= 12 and hour <18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("i am alfraid ,sir, please tell me how may i help you? ")
#it will take my voice from microphone as command
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........ ")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"User said :  {query}\n")
    except Exception as e:
        #print(e)
        print("Could not recognize please say that again sir........")
        return "None"
    return query
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()                                         #change email,password first & enable less secure apps access on your email id
    server.login('your_email','your password')
    server.sendmail('your_email',to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("http://youtube.com/")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/aftab.mallick.146")
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/aftab-mallick/")
        elif 'open google' in query:
            webbrowser.open("http://google.com/")
        elif 'open stackoverflow' in query:
            webbrowser.open("http://stackoverflow.com/")
        elif 'play music' in query:
            music_dir ='D:\songs'                  #copy your songs library location
            songs=os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is {strtime}")
        elif 'send email' in query:
            try:
                speak("Sir,tell me your message")
                content = takeCommand()
                to ='enter email receiver email'
                sendEmail(to,content)
                speak("Email has been send ,sir,anything else may i help with ")
            except Exception as e:
                print(e)
                speak("Sorry sir due to some technical issues i could not full fill your request        anything else may i help with ")
        elif 'quit' in query:
            sys.exit()
        elif 'none' in query:
            speak("Could not recognize please say that again sir")
        else:
            query=query.replace("open","")
            pwt.search(query)
