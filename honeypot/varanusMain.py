import sys
import os
import time
import phoneCheck
import sendAlert

textLen = phoneCheck.newTexts()
callLen = phoneCheck.newCalls()
#callLen = 1

while 1:
    check = phoneCheck.newTexts()
    if check > textLen:
        print("#####ALERT TEXT#####")
        sendAlert.alert("SOMEBODY TEXTING ME....HELP PLS")
        textLen = check

    check = phoneCheck.newCalls()
    if check > callLen:
        print("#####ALERT CALL#####")
        sendAlert.alert("SOMEBODY CALLING ME....HELP PLS")
        callLen = check
    time.sleep(30)
