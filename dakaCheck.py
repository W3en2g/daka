import cv2
import numpy as np
import datetime

def checkResult(user):
    path = r"/home/daka/expectedResult.png"
    expectedAns = cv2.imread(path)
    today = datetime.date.today()
    today = str(today)
    patha = r"/home/daka/log/"+user+"/"+today+".png"
    ans=cv2.imread(patha)
    print(patha)
    difference = cv2.subtract(expectedAns, ans)
    result = not np.any(difference)
    if result:
        print(user," is done")
    else:
        print("has problem for ", user, " try again now")
    print("-----------------------------------------")
    return result
