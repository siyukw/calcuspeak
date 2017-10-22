from gtts import gTTS
import subprocess
import os
from pathlib import Path
from pygame import mixer # Load the required library



#import cgi

#form = cgi.FieldStorage()

def text_to_speech(answer):
	tts = gTTS(text=answer, lang='en')
	if (Path("./answer.mp3").is_file()):
		os.remove("./answer.mp3")
	tts.save("answer.mp3")
	audio_file = "./answer.mp3"
	mixer.init()
	mixer.music.load('./answer.mp3')
	mixer.music.play()
	#subprocess.call(["afplay", audio_file])

#text_to_speech(form.getvalue("text"))
