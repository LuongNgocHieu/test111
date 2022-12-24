from tkinter import *
import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3
print(googletrans.LANGUAGES)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print('Khu tieng on..')
    recognizer.adjust_for_ambient_noise(source, duration = 1)
    print('please speak')
    audio = recognizer.listen(source, timeout = 5)
try:
    print('Dang nhan dang')
    result = recognizer.recognize_google(audio, language = 'en')
except Exception as ex:
    print(ex)

def trans():
    langinput = input('Language you want to trans to')
    translator = google_translator()
    translate_text = translator.translate(str(result),lang_tgt = str(langinput))
    print(translate_text)
    engine.say(str(translate_text))
    engine.runAndWait()
trans()
