import calculator, textToAudio, audioToText

data = audioToText.audioToText()
# if null, run again
print(data)
sol = calculator.calculate(data)
print(sol)
textToAudio.text_to_speech(sol)
#
