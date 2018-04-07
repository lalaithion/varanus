from getNewTexts import newTexts
import time

textLen = 0
callLen = 0


while 1:
	check = newTexts()
	if check > textLen:
		alert.alertText()
		alertSpark.alertText()
		textLen = check
	check = newCalls()
	if check > callLen:
		alert.alertCall()
		alertSpark.slertCall()
	time.sleep(30)

