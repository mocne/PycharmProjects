# coding:utf-8
import subprocess
from PIL import Image
from PIL import ImageOps
from selenium import webdriver
import time, os, sys


def cleanImage(imagePath):
    image = Image.open(imagePath)  # 打开图片
    image = image.point(lambda x: 0 if x < 143 else 255)  # 处理图片上的每个像素点，使图片上每个点“非黑即白”
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)

def getAuthCode(driver, url="http://localhost/"):
    captchaUrl = url + "common/random"
    driver.get(captchaUrl)
    time.sleep(0.5)
    driver.save_screenshot("captcha.jpg")  # 截屏，并保存图片
    # urlretrieve(captchaUrl, "captcha.jpg")
    time.sleep(0.5)
    cleanImage("captcha.jpg")
    p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout= \
        subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("captcha.txt", "r")

    # Clean any whitespace characters
    captchaResponse = f.read().replace(" ", "").replace("\n", "")

    print("Captcha solution attempt: " + captchaResponse)
    if len(captchaResponse) == 4:
        return captchaResponse
    else:
        return False


def withoutCookieLogin(url="http://org.cfu666.com/"):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    while True:
        authCode = getAuthCode(driver, url)
        if authCode:
            driver.back()
            driver.find_element_by_xpath("//input[@id='orgCode' and @name='orgCode']").clear()
            driver.find_element_by_xpath("//input[@id='orgCode' and @name='orgCode']").send_keys("orgCode")
            driver.find_element_by_xpath("//input[@id='account' and @name='username']").clear()
            driver.find_element_by_xpath("//input[@id='account' and @name='username']").send_keys("username")
            driver.find_element_by_xpath("//input[@type='password' and @name='password']").clear()
            driver.find_element_by_xpath("//input[@type='password' and @name='password']").send_keys("password")
            driver.find_element_by_xpath("//input[@type='text' and @name='authCode']").send_keys(authCode)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            try:
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='side-menu']/li[2]/ul/li/a").click()
                return driver
            except:
                print("authCode Error:", authCode)
                driver.refresh()
    return driver


driver = withoutCookieLogin("http://www.cnaidai.com/")
driver.get("http://localhost/enterprise/add/")