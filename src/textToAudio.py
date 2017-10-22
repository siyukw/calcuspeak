from gtts import gTTS
import subprocess
import os
#import cgi

#form = cgi.FieldStorage()

def text_to_speech(answer):
    tts = gTTS(text=answer, lang='en')
    tts.save("answer.mp3")
    audio_file = "./answer.mp3"
    subprocess.call(["afplay", audio_file])
    os.remove("./answer.mp3")

#text_to_speech(form.getvalue("text"))
