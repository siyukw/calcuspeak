from gtts import gTTS
import subprocess
import os
import time
from pathlib import Path
from pygame import mixer # Load the required library



#import cgi

#form = cgi.FieldStorage()

def text_to_speech(answer):
	tts = gTTS(text=answer, lang='en')
	#if (Path("./answer.mp3").is_file()):
	tts.save("answer.mp3")
	mixer.init()
	mixer.music.load('./answer.mp3')
	mixer.music.play()
	time.sleep(15)
	os.remove("./answer.mp3")
	#subprocess.call(["afplay", audio_file])

#text_to_speech(form.getvalue("text"))