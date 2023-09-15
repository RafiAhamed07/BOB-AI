import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5') #for voice
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id) # 0 for boy & 1 for girl
boy = "BOB"
girl = "Jeni"
user_name = "" #pleasr place you system user name here

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good morning")
    
    elif hour>= 12 and hour < 12:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
        
    speak(f"Sir I am {boy}. Please tell me how may I help you")

def takeCommand():
    '''It takes microphone input from the users  and returns string outpu'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print("Recogniging.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

    
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
         # logic for exicuting the tasks based on query 
        if 'wikipedia' in query:
             speak("Searching wikipedia......")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("According tp wikipedia")
             print(results)
             speak(results)
             
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
            
        
        elif 'play music' in query:
            a = random.randint(1,94)
            music_dir =  'D:\\musics'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[a]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is{strTime}")
        
        elif 'open code' in query:
            codePath = f"C:\\Users\\{user_name}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'quit' in query:
            speak("Shouting down....")
            exit()
        elif 'exit' in query:
            speak("Shouting down....")
            exit()
        elif 'shoutdown' in query:
            speak("Shuting down....")
            exit()
    
        elif 'thank you' in query:
            speak("Welcome sir.This is my duty")
        elif 'how are you' in query:
            speak("I am good sir.How can I help you sir?")
