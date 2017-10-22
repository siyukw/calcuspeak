import speech_recognition as sr
import pyaudio

def audioToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = "1a7933ab6deb4875ae7fe8da33cd9eff"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        return r.recognize_bing(audio, key=BING_KEY)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
