import sys
import os
import time
import phoneCheck
import sendAlert

textLen, number = phoneCheck.newTexts()
callLen, number = phoneCheck.newCalls()
#callLen = 1

while 1:
    check, number = phoneCheck.newTexts()
    print(check)
    print(number)
    if check > textLen:
        print("#####ALERT TEXT#####")
        sendAlert.alert("SOMEBODY TEXTING ME....HELP PLS", number)
        textLen = check+1
    check, number = phoneCheck.newCalls()
    print(check, number)
    if check > callLen:
        print("#####ALERT CALL#####")
        sendAlert.alert("SOMEBODY CALLING ME....HELP PLS", number)
        callLen = check+1
    time.sleep(15)
