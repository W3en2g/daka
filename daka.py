from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import undetected_chromedriver.v2 as uc
import requests
import cv2
from recoPic import getDistance 
from dakaCheck import checkResult
import logging
logging.basicConfig(filename='/home/daka/record/log', level=logging.ERROR,format='%(asctime)s %(message)s')

def dakarun(theID,thePassw):
    message = "run for "+theID
    logging.info(message)
    print("run for ",theID)

    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    options.add_argument('--headless')
    wd = uc.Chrome(options=options)


    wd.get('https://stuhealth.jnu.edu.cn/#/login')
    print(wd.title)

    script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
 
    #运行Javascript
    wd.execute_script(script)
    wd.implicitly_wait(20)
    wd.find_element(By.ID, 'zh').send_keys(theID)
    wd.find_element(By.ID, 'passw').send_keys(thePassw)
    slider = wd.find_element(By.CLASS_NAME, 'yidun_slider')
    slider.click()
    sleep(4) 
    background_image_url = wd.find_element(By.XPATH,'/html/body/app-root/app-login/div[2]/div[2]/form/div[3]/div/div[1]/div/div[1]/img[1]').get_attribute('src')
    background_image = requests.get(background_image_url).content

    background_image_path = '/home/daka/background_image' + '.jpg'
    print(background_image_path)
    with open(background_image_path, mode='wb') as f:
        f.write(background_image)
        f.close()
        sleep(3)
        distance = getDistance(background_image_path)-20
        print("The distance is ",distance)
        sleep(1)
        ActionChains(wd).drag_and_drop_by_offset(slider,distance,0).perform()
        sleep(1)
        wd.find_element(By.XPATH,'/html/body/app-root/app-login/div[2]/div[2]/form/div[5]/div/button').click()


        try:
            wd.find_element(By.ID,'10000').click()
            sleep(1)
            wd.find_element(By.ID,'tj').click()

        except:
            pass
        finally:
            sleep(2)
            today = datetime.date.today()
            today = str(today)
            result_img_path = "/home/daka/record/"+theID+"/"+today+'.png'
            try:
                result_image_url = wd.find_element(By.XPATH,'/html/body/app-root/app-index/div/div[1]/app-complete/section/section/div/div/div/div/div/div[1]/img').get_attribute('src')
                result_image = requests.get(result_image_url).content
                with open(result_img_path, mode='wb') as f:
                    f.write(result_image)
                    f.close()
            except:
                pass
            wd.close() 
            sleep(3)
            pass


def mainrun(userid,password):
    sucess = checkResult(userid)
    if sucess:
        return True
    while(not sucess):
        dakarun(userid,password)
        sucess = checkResult(userid)
    return False

