import sys
import os
import time
sys.path.append(os.getcwd()+"/phone")
from getNewTexts import newTexts
from getNewCalls import newCalls
sys.path.append(os.getcwd()+"/alerts")
from alertPhone import alertText

textLen = newTexts()
callLen = newCalls()

while 1:
	check, number = newTexts()
	if check > textLen:
		print("alertText")
		alertText()
		#alertSpark.alertText()
		textLen = check
	check, number = newCalls()
	if check > callLen:
		print("alertCall")
		alertCall()
		#alertSpark.slertCall()
	time.sleep(30)

