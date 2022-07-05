import cv2
import numpy as np
import datetime
import logging
logging.basicConfig(filename='/home/daka/record/log', level=logging.INFO,format='%(asctime)s %(message)s')
def checkResult(user):
    path = r"/home/daka/expectedResult.png"
    expectedAns = cv2.imread(path)
    today = datetime.date.today()
    today = str(today)
    patha = r"/home/daka/record/"+user+"/"+today+".png"
    try:
        ans=cv2.imread(patha)
        print(patha)
        difference = cv2.subtract(expectedAns, ans)
        result = not np.any(difference)
        if result:
            message = user +" is done"
            logging.info(message)
            print(user," is done")
        else:
            message = "has problem for ", user, " try again now"
            logging.warning(message)
            print("has problem for ", user, " try again now")
        print("-----------------------------------------")
        return result
    except:
        return False
