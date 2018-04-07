import sys
import os
sys.path.append(os.getcwd()+"/phone")
from getNewTexts import newTexts
import time

textLen = newTexts()
callLen = newCalls()

while 1:
	check = newTexts()
	if check > textLen:
		print("alertText")
		#alert.alertText()
		#alertSpark.alertText()
		textLen = check
	check = newCalls()
	if check > callLen:
		print("alertCall")
		#alert.alertCall()
		#alertSpark.slertCall()
	time.sleep(30)

