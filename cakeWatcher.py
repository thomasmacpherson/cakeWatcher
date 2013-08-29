from espeak import espeak
import pifacedigitalio as piface
piface.init()

import os

statements = ("Close this door now", "You will regret it tomorrow","A moment on the lips you know the rest")
numberOfStatements = len(statements)
currentStatement = 0

inputPin = 0


while True:
	if piface.digital_read(inputPin):
		statement = statements[currentStatement%numberOfStatements]
		print statement
		speakCall = "espeak '" + statement + "' 2>/dev/null"
		os.system(speakCall)
		currentStatement+=1

		while piface.digital_read(inputPin):
			pass
