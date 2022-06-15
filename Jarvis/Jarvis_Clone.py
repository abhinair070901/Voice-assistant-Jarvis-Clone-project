import speech_recognition as sr
import pyttsx3 as py
import pywhatkit
import datetime
import wikipedia
import pyjokes
listner = sr.Recognizer()
engine = py.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is' + time)
    elif 'tell me about' in command:
        Knowledge = command.replace('tell me about','')
        info = wikipedia.summary(Knowledge, 3)
        print(info)
        talk(info)
    elif 'are you human' in command:
        talk('No,but i can help you with your needs')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
while True:
    run_jarvis()
