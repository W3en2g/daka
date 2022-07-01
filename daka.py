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

# https://blog.csdn.net/qq_36078992/article/details/110326518
def dakarun(theID,thePassw):
    # 加上参数，禁止 chromedriver 日志写屏
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # # options.add_argument("window-size=1024,768")
    # options.add_argument("--no-sandbox")

    # options.add_argument("--disable-blink-features")
    # options.add_argument("--disable-blink-features=AutomationControlled")
    # wd = webdriver.Chrome(r'/home/daka/chromedriver',options=options)

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
        print(distance)
        sleep(1)
        # slider = wd.find_element(By.CLASS_NAME, 'yidun_slider')
        ActionChains(wd).drag_and_drop_by_offset(slider,distance,0).perform()
        sleep(1)
        wd.find_element(By.XPATH,'/html/body/app-root/app-login/div[2]/div[2]/form/div[5]/div/button').click()

        #random temperture

        try:
            # wd.find_element(By.ID, 'cjtw').send_keys("36.2")
            # wd.find_element(By.ID, 'wujtw').send_keys("36.3")
            # wd.find_element(By.ID, 'wajtw').send_keys("36.3")
            # wd.find_element(By.ID, 'twyjcrq').send_keys(Keys.ENTER)
            # wd.find_element(By.ID, 'twejcrq').send_keys(Keys.ENTER)
            # wd.find_element(By.ID, 'twsjcrq').send_keys(Keys.ENTER)
            wd.find_element(By.ID,'10000').click()
            sleep(1)
            wd.find_element(By.ID,'tj').click()
            # wd.find_element(By.XPATH,'/html/body/app-root/app-index/div/div[1]/app-home/section/section/div/div/div/div/div/div[44]/button').click()

        except:
            pass
        finally:
            sleep(2)
            today = datetime.date.today()
            today = str(today)
            resultimg = "/home/daka/log/"+theID+"/"+today+'.png'
            wd.save_screenshot(resultimg)
            wd.close() 
            pass




