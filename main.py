import pyttsx3 as p
import speech_recognition as sr
from selenium_webpage import *
from yt import *
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("hello sir i am your voice assistant. how are you?")

with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you??")

with sr.Microphone() as source:
    r.energy_threshold = 1000
    r.adjust_for_ambient_noise(source,1.2)
    print("listnening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    
if "information" in text2:
    speak("you need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,1.2)
        print("listnening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    assist=infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("you want me to play which video")
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source,1.2)
        print("listnening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    speak("Playing {} on youtube".format(vid))
    print("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)