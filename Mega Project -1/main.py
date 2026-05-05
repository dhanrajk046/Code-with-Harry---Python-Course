# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# from openai import OpenAI
# from gtts import gTTS
# import pygame
# import os

# # pip install pocketsphinx

# recognizer = sr.Recognizer()
# engine = pyttsx3.init() 
# newsapi = "<Your Key Here>"

# def speak_old(text):
#     engine.say(text)
#     engine.runAndWait()

# def speak(text):
#     tts = gTTS(text)
#     tts.save('temp.mp3') 

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the MP3 file
#     pygame.mixer.music.load('temp.mp3')

#     # Play the MP3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
#     pygame.mixer.music.unload()
#     os.remove("temp.mp3") 

# def aiProcess(command):
#     client = OpenAI(api_key="<Your Key Here>",
#     )

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         r = requests.get(f"")
#         if r.status_code == 200:
#             # Parse the JSON response
#             data = r.json()
            
#             # Extract the articles
#             articles = data.get('articles', [])
            
#             # Print the headlines
#             for article in articles:
#                 speak(article['title'])

#     else:
#         # Let OpenAI handle the request
#         output = aiProcess(c)
#         speak(output) 





# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
         
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                 speak("Ya")
#                 # Listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommand(command)


#         except Exception as e:
#             print("Error; {0}".format(e))


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from groq import Groq
from groq import GroqError
# pip install pocketsphinx






recognizer = sr.Recognizer()
engine = pyttsx3.init() 
# newsapi = ""



import os
from groq import Groq


client = Groq(api_key="")



# client = Groq(api_key="GROQ_API_KEY")

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

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

# def aiProcess(command):
#     client = Grok(api_key="")

#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
#         {"role": "user", "content": command}
#     ]
#     )

#     return completion.choices[0].message.content


def aiProcess(command: str) -> str:
    for model in ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are Jarvis. Virtual AI Assistant. Give short and 5 important sentences responses and make conversation with user. You are very intelligently."},
                    {"role": "user", "content": command},
                ],
                temperature=0.4,
                max_tokens=150,
            )
            return completion.choices[0].message.content
        except GroqError as e:
            # try next model
            last_err = e
    return f"Model error: {last_err}"



# def aiProcess(command: str) -> str:
#     completion = client.chat.completions.create(
#         model="llama-3.1-70b-versatile",
#         messages=[
#             {"role": "system", "content": "You are Jarvis. Virtual AI Assistant. Give short responses."},
#             {"role": "user", "content": command},
#         ],
#         temperature=0.4,
#         max_tokens=150,
#     )
#     return completion.choices[0].message.content


def processCommand(c):
    c_lower = c.lower()

    if "open google" in c_lower:
        webbrowser.open("https://google.com")

    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")

    elif c_lower.startswith("play"):
        song = c_lower.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library.")

    elif "news" in c_lower:
        url = ""
        params = {
            "apikey": "",
            "language": "en",
            # "country": "in",
        }

        try:
            r = requests.get(url, params=params, timeout=15)
            if r.status_code != 200:
                print("News API error:", r.status_code, r.text[:300])
                speak("Sorry, I couldn't fetch the news right now.")
                return

            data = r.json()
            articles = data.get("results") or data.get("articles") or []

            if not articles:
                speak("I couldn't find any news right now.")
            else:
                speak("Here are the latest headlines.")
                for article in articles[:5]:
                    title = article.get("title")
                    if title:
                        speak(title)

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            speak("Sorry, there was a network issue while fetching news.")

    else:
        output = aiProcess(c)
        speak(output)

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

    

#     elif "news" in c.lower():
#     #   url = "https://newsdata.io/api/1/latest"
#       params = {
#         "apikey": "",
#         "language": "en",     # optional
#         # "country": "in",    # optional
#     }



#     try:
#         r = requests.get(url, params=params, timeout=15)
#         if r.status_code != 200:
#             print("News API error:", r.status_code, r.text[:300])
#             speak("Sorry, I couldn't fetch the news right now.")
#         else:
#             data = r.json()

#             # Newsdata usually uses 'results'
#             articles = data.get("results") or data.get("articles") or []

#             if not articles:
#                 speak("I couldn't find any news right now.")
#             else:
#                 speak("Here are the latest headlines.")
#                 for article in articles[:5]:  # limit to 5
#                     title = article.get("title")
#                     if title:
#                         speak(title)

#     except requests.exceptions.RequestException as e:
#         print("Request failed:", e)
#         speak("Sorry, there was a network issue while fetching news.")


#     else:
#         # Let OpenAI handle the request
#         output = aiProcess(c)
#         speak(output) 



    # elif "news" in c.lower():
    #     r = requests.get(f"")
    #     if r.status_code == 200:
    #         # Parse the JSON response
    #         data = r.json()
            
    #         # Extract the articles
    #         articles = data.get('articles', [])
            
    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])

    # else:
    #     # Let OpenAI handle the request
    #     output = aiProcess(c)
    #     speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=4, phrase_time_limit=2)

                # audio = r.listen(source, timeout=4, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


