import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
text = 'Hello Sir, I am Jarvis. How can I help you?'
def talk(text):
    engine.say(text)
    engine.runAndWait()
talk(text)
try:
    with sr.Microphone() as source:

        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'jarvis' in command:
            print(command)
except:
    pass