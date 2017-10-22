from gtts import gTTS
import subprocess


def text_to_speech(answer):
        tts = gTTS(text='The answer is ' + answer, lang='en')
        tts.save("answer.mp3")
        audio_file = "./answer.mp3"
        subprocess.call(["afplay", audio_file])


if __name__ == "__main__":
    text_to_speech("y = 5x")
