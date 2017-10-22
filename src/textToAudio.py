from gtts import gTTS
import subprocess
import os

def text_to_speech(answer):
        tts = gTTS(text=answer, lang='en')
        tts.save("answer.mp3")
        audio_file = "./answer.mp3"
        subprocess.call(["afplay", audio_file])
        os.remove("./answer.mp3")

if __name__ == "__main__":
    text_to_speech("the answer is x = minus i root (57), y = 5")
