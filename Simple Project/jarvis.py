import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
listner = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening..........")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def first():
    print('Hi! My name is alexa. I am your personal assistant. Please command me anything')
    talk('hi! My name is alexa. I am your personal assistant. Please command me anything') 

def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'current time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk(time)
    elif 'say something about' in command:
        person = command.replace('say something about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'jokes' in command:
        print(pyjokes.get_jokes())
        talk(pyjokes.get_jokes())
    elif 'google' in command:
        webbrowser.open('google.com')
        talk('opening google')
    elif 'stackoverflow' in command:
        talk('opening stackoverflow')
        webbrowser.open('stackoverflow.com')
    elif 'code' in command:
        talk('opening Vs code')
        codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'chrome' in command:
        talk('opening chrome')
        chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chromePath)
    elif 'pycharm' in command:
        talk('opening pycharm')
        pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3\\bin\\pycharm64.exe"
        os.startfile(pyPath)
    elif 'firefox' in command:
        talk('opening firefox')
        foxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(foxPath)
    elif 'who is your creator' in command:
        print('my creator is talha mahamud')
        talk('my creator is Talha Mahamud')
    elif 'are you married' in command:
        print('No. But I am wating for get married with siri. We love each other.')
        talk('No. But I am wating for get married with siri. We love each other')
    elif 'have you any girlfriend' in command:
        talk('Yes, his name is siri')
    elif 'do you know siri' in command:
        talk('yes! she is my girlfriend. i love him so much!')
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'who are you' in command:
        print('I am personal assistent of you')
        talk('i am personal assistent of you')
    elif 'sadi' in command:
        talk('sadi is the cousine of my creator')


if __name__ == '__main__':
    # first()
    while True:
        run_alexa()
