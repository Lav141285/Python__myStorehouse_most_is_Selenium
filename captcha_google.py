import random
import time
# selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# recaptcha libraries
import speech_recognition as sr

import urllib
import pydub


def delay():
    time.sleep(random.randint(2, 3))


try:
    # create chrome driver
    driver = webdriver.Chrome(r"D:\ChromeDriver\chromedriver.exe")
    delay()
    # go to website
    driver.get("https://www.google.com/recaptcha/api2/demo")

except:
    print("[-] Please update the chromedriver.exe")

# switch to recaptcha frame
frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[0])
delay()
# click on checkbox to activate recaptcha
driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
# switch to recaptcha audio control frame
driver.switch_to.default_content()
frames = driver.find_element(
    By.XPATH, "/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()
# click on audio challenge
driver.find_element(By.ID, "recaptcha-audio-button").click()
# switch to recaptcha audio challenge frame
driver.switch_to.default_content()
frames = driver.find_elements(By.TAG_NAME, "iframe")
driver.switch_to.frame(frames[-1])
delay()
# click on the play button
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/button").click()
delay()

# get the mp3 audio file
src = driver.find_element(By.ID, "audio-source").get_attribute("src")
print("[INFO] Audio src: %s" % src)
# download the mp3 audio file from the source
urllib.request.urlretrieve(src, "D:\\Garbage\\sample.mp3")
#pydub.AudioSegment.ffmpeg = "E:\\ffmpeg-N-103323-g252128561e-win64-gpl\\bin\\ffmpeg.exe"
sound = pydub.AudioSegment.from_mp3("D:\\Garbage\\sample.mp3")
sound.export("D:\\Garbage\\sample.wav", format="wav")
sample_audio = sr.AudioFile("D:\\Garbage\\sample.wav")
print('[+] Audio Saved')
r = sr.Recognizer()
with sample_audio as source:
    audio = r.record(source)
key = r.recognize_google(audio)
print('[INFO] Recaptcha Passcode:', key)
#key in results and submit
driver.find_element(By.ID, "audio-response").send_keys(key.lower())
driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
delay()
driver.find_element(By.ID, "recaptcha-demo-submit").click()
delay()
