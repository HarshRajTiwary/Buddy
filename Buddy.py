import pyttsx3 as ps
import os
import speech_recognition as sr
import subprocess
#connect to open ai

def speak(text):
    engine = ps.init()
    engine.say(text)
    engine.runAndWait()

hlo = ["hello", "hi", "hello buddy", "Hello Buddy", "hello body"]
ch1 = ["yes", "y", "Yes", "Y", "YES"]
ch2 = ["no", "n", "N", "NO", "No"]

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
        except sr.RequestError:
            print("Sorry, could not connect to the speech recognition service")

    if text in hlo:
        print("Welcome to Harsh Project. How can I help you?")
        speak("Welcome to Harsh Project. How can I help you?")
        text="Sorry! could not listen what you said"

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
        text="Sorry! could not listen what you said"

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
        text="Sorry! could not listen what you said"

    elif text == "how are you":
        print("I am fine, thank you. And what about you?")
        speak("I am fine, thank you. And what about you?")
        text="Sorry! could not listen what you said"

    elif text == "I am fine" or text == "I am also fine" or text == "I am fine too":
        print("Good to hear. Hope you always stay fine and energetic.")
        speak("Good to hear. Hope you always stay fine and energetic.")
        text="Sorry! could not listen what you said"

    elif text == "who created you":
        print("Harsh Raj created me. I am Buddy, a virtual assistant.")
        speak("Harsh Raj created me. I am Buddy, a virtual assistant.")
        text="Sorry! could not listen what you said"

    elif text == "how do you do":
        print("I am fine, thank you. And what about you?")
        speak("I am fine, thank you. And what about you?")
        text="Sorry! could not listen what you said"

    elif text == "what's your name":
        print("I am Buddy, a virtual assistant.")
        speak("I am Buddy, a virtual assistant.")
        text="Sorry! could not listen what you said"

    elif text == "what's going on":
        print("hmm, interacting with you. ")
        speak("hmm, interacting with you. ")
        text="Sorry! could not listen what you said"

    elif text == "open Notepad":
        print("Opening notepad. ")
        speak("opening notepad. ")
        subprocess.Popen("notepad.exe")
        text="Sorry! could not listen what you said"