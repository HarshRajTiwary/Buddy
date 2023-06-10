import pyttsx3 as ps
import os
import speech_recognition as sr
import subprocess

# Connect to OpenAI

def speak(text):
    engine = ps.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

hlo = ["hello", "hi", "hello buddy", "Hello Buddy", "hello body"]
ch1 = ["yes", "y", "Yes", "Y", "YES"]
ch2 = ["no", "n", "N", "NO", "No"]
ext = ["tanks","thank you","thank you so much","exit","thanks"]

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Sorry, could not recognize what you said")
            continue
        except sr.RequestError:
            print("Sorry, could not connect to the speech recognition service")
            continue

    if text in hlo:
        print("Welcome to Harsh Project. How can I help you?")
        speak("Welcome to Harsh Project. How can I help you?")
        continue

    elif text == "shutdown":
        print("Enter yes or no.")
        speak("Enter yes or no.")
        a = input("Enter yes/no: ")
        if a in ch1:
            print("Shutting down your PC in 30 seconds.")
            speak("Shutting down your PC in 30 seconds.")
            os.system("shutdown /s /t 30")
        elif a in ch2:
            print("Shutdown aborted.")
            speak("Shutdown aborted.")
        continue

    elif text == "restart":
        print("Enter yes or no.")
        speak("Enter yes or no.")
        a = input("Enter yes/no: ")
        if a in ch1:
            print("Restarting your PC in 30 seconds.")
            speak("Restarting your PC in 30 seconds.")
            os.system("shutdown /r /t 30")
        elif a in ch2:
            print("Restart aborted.")
            speak("Restart aborted.")
        continue

    elif text == "how are you":
        print("I am fine, thank you. And what about you?")
        speak("I am fine, thank you. And what about you?")
        continue

    elif text in ["I am fine", "I am also fine", "I am fine too"]:
        print("Good to hear. Hope you always stay fine and energetic.")
        speak("Good to hear. Hope you always stay fine and energetic.")
        continue

    elif text == "who created you":
        print("Harsh Raj created me. I am Buddy, a virtual assistant.")
        speak("Harsh Raj created me. I am Buddy, a virtual assistant.")
        continue

    elif text == "how do you do":
        print("I am fine, thank you. And what about you?")
        speak("I am fine, thank you. And what about you?")
        continue

    elif text == "what's your name":
        print("I am Buddy, a virtual assistant.")
        speak("I am Buddy, a virtual assistant.")
        continue

    elif text == "what's going on":
        print("Hmm, interacting with you.")
        speak("Hmm, interacting with you.")
        continue

    elif text == "open Notepad":
        print("Opening Notepad.")
        speak("Opening Notepad.")
        subprocess.Popen("notepad.exe")
        continue

    elif text in ext:
        print("Thank you for interacting with me, this made me happy. ")
        speak("Thank you for interacting with me, this made me happy. ")
        break