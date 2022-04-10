from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\Tesseract.exe'


def initDriver(filepath):

	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\'+ filepath) 
	'''
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	'''
	browser = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', chrome_options=options)
	return browser 

tang=0
if __name__ == '__main__':
	while(1):
		taikhoan =  ("tieple247",'tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
		taikhoanx = taikhoan[tang]
		driver = initDriver(taikhoanx)
		print(taikhoanx)
		driver.get("https://facebook.com")
		input()
		#time.sleep(2)
		try:
			driver.quit()
		except:
			time.sleep(0)
		tang+=1