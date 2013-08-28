from espeak import espeak
import pifacedigitalio as piface
piface.init()

statements = ("Close this door now", "You will regret it tomorrow","A moment on the lips, you know the rest")
numberOfStatements = len(statements)
currentStatement = 0

inputPin = 0


while True:
	if piface.digital_read(inputPin):
		espeak.synth(statements[currentStatement%numberOfStatements])
		print statements[currentStatement%numberOfStatements]
		currentStatement+=1
		while piface.digital_read(inputPin):
			pass