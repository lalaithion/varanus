import sys
import os
import time
import phoneCheck
import sendAlert

textLen = phoneCheck.newTexts()
callLen = phoneCheck.newCalls()

while 1:
	check = phoneCheck.newTexts()
	if check > textLen:
		print("alertText")
		#alertText()
		sendAlert.alert("SOMEBODY TEXTING ME....HELP PLS")
		#alertSpark.alertText()
		textLen = check
	check = phoneCheck.newCalls()
	if check > callLen:
		print("alertCall")
		#alertCall()
		sendAlert.alert("SOMEBODY CALLING ME....HELP PLS")
		#alertSpark.slertCall()
	time.sleep(30)

