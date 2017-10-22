import calculator, textToAudio, audioToText

def q():
    data = audioToText.audioToText()
    print(data)
    sol = calculator.calculate(data)
    print(sol)
    textToAudio.text_to_speech(sol)
