import calculator, textToAudio, audioToText

data = audioToText.audioToText()
sol = calculator.calculate(data)
textToAudio.text_to_speech(sol)
