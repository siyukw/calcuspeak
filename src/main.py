import calculator, textToAudio, audioToText

def main():
    data = audioToText.audioToText()
    print(data)
    sol = calculator.calculate(data)
    print(sol)
    textToAudio.text_to_speech(sol)
