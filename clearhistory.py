from selenium import webdriver
import time
import pyautogui
def initDriver(filepath):
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=D:\Golike\CrawlJob\src\main\resources\data\tieple247')
	options.add_argument("start-maximized")
	
	options.add_argument("start-maximized")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	options.add_argument("--disable-blink-features")
	options.add_argument("--disable-blink-features=AutomationControlled")
	
	prefs = {
	"profile.managed_default_content_settings.images":1
	}
	
	options.add_experimental_option("prefs",prefs)
	
	driver = webdriver.Chrome(executable_path=r'c:\\withpython\\chromedriver.exe', options=options)
	return driver

tang=3
if __name__ == '__main__':
	while(1):
		taikhoan =  ('tieple247','tieple02','happier_in_2021_3','happier_in_2021_4','happier_in_2021_5','happier_in_2021_6','happier_in_2021_8')

		if((tang) > len(taikhoan)-1):
			break
		taikhoanx = taikhoan[tang]
		print (taikhoanx)
		driver = initDriver(taikhoanx)
		input()
		'''
		driver.get('chrome://settings/content/siteDetails?site=https%3A%'+'2F%'+'2Fmbasic.facebook.com')
		time.sleep(1)
		pyautogui.click(1017, 701)
		time.sleep(1)
		pyautogui.click(1016, 751)
		time.sleep(0.5)
		'''
		driver.get('chrome://settings/clearBrowserData')
		#time.sleep(0.5)
		#pyautogui.click(1050, 621)
		#time.sleep(0.5)
		#pyautogui.click(571, 581)
		time.sleep(1)
		'''
		chrome://settings/content/siteDetails?site=https%3A%2F%2Fmbasic.facebook.com
		if(tang % 2 == 0):
			driver.set_window_position(0, 0, windowHandle ='current')
			driver.set_window_size(800, 600)
			time.sleep(1)
			pyautogui.click(597,558)
		else:
			driver.set_window_position(800, 0, windowHandle ='current')
			driver.set_window_size(800, 600)
			time.sleep(1)
			pyautogui.click(1396, 566)
		'''
		#driver.get("https://mbasic.facebook.com/")
		
		pyautogui.click(1023, 685)
		time.sleep(4)
		input()
		driver.quit()
		
		tang+=1