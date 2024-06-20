import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI, completions
from gtts import gTTS
import pygame
import os


#pip install pocketsphinx

recognizer = sr.Recognizer()
engine= pyttsx3.init()
newsapi =  "64bdff3681854bb4b2c82d4ffc46d4d2"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3") 

    def speak(text):
      
      tts = gTTS(text)
      tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def airProcess(command):
    client = OpenAI(api_key="sk-proj-OIbY24fgySDRTpGsEPxMT3BlbkFJKqOIzvgcBkiuvAIxriwq"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named kumar, skilled in skilled in general taskslike Alexa and google cloude.Give short responses"},
            {"role": "user", "content": command}
        ]
        )

    return completion.choice[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get("articles", [])

            for article in articles:
                speak(article["title"])
    else:
        output = airProcess(c)
        speak(output)
        

       

if __name__ == "__main__":
    speak("Initializing Kumar....")

    while True:
        #Listen for the wake word kumar
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using google-cloud
        print("recognizing...")
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source, timeout=6,phrase_time_limit=1)
            word = command = r.recognize_google_cloud(audio)
            if(command.lower() == "kumar"):
                speak("yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Kumar active...")
                    audio = r.listen(source)
                    command = r.recognize_google_cloud(audio)

                    processCommand(command)


            
        except sr.RequestError as e:
            print("google errors; {0}".format(e))
