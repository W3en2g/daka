import cv2
import numpy as np


oriList = []
path = r"/home/daka/1.png"
ori=cv2.imread(path)
oriList.append(ori)
path = r"/home/daka/2.png"
ori=cv2.imread(path)
oriList.append(ori)
path = r"/home/daka/3.png"
ori=cv2.imread(path)
oriList.append(ori)
path = r"/home/daka/4.png"
ori=cv2.imread(path)
oriList.append(ori)
path = r"/home/daka/5.png"
ori=cv2.imread(path)
oriList.append(ori)

def getDistance(path):
    patha = r"/home/daka/background_image.jpg"
    polluted=cv2.imread(patha)

    # cv2.waitKey()
    distance = 159
    for ori in oriList:
        res = ori - polluted

        r = 0
        l = 0

        found = False
        for w in range(0,320):
          for h in range(0,160):
            if int(res[h,w,0])+int(res[h,w,1])+int(res[h,w,2])!=0:
              l = w
              found = True
              break
          if found is True: 
              break

        found = False
        for w in range(319,-1,-1):
          for h in range(0,160):
            if int(res[h,w,0])+int(res[h,w,1])+int(res[h,w,2])!=0  :
              r = w
              found = True
              break
          if found is True:
              break

        if ((l+r)//2)!=159:
            distance=((l+r)//2)
            # for w in range(0,320):
            #     for h in range(0,160):
            #         if w == (l+r)//2:
            #             res[h,w] = [255,255,255]
            # cv2.imshow("",res)
            # cv2.waitKey()

    return distance



