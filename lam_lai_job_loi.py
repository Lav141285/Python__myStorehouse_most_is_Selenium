from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from playsound import playsound
from PIL import Image
import pytesseract as pt
from pytesseract import image_to_string
import time 
import random,os,re
from multiprocessing import Pool
from datetime import datetime
pt.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\Tesseract.exe'
tang=0

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

def lamviec_lm_lai ():
	global golike,countfage,sojobhuy,tongsojob,tang
	try:
		WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/a")))
		try:
			job = driver.find_elements_by_tag_name("a")
			
			# nut hoan thanh
		except:
			print("không lấy dc các nút ")
		x=0
		
		while(x <len(job)-23):
			winds = driver.window_handles
			for wind in winds:
				if(wind != golike):
					driver.switch_to.window (wind)
					driver.close()
			driver.switch_to.window (golike)
			job = driver.find_elements_by_tag_name("a")
			add = driver.find_elements_by_tag_name("span") # để biết đây là loại job gì 5 + x * 5 
			print(x)
			d = job[x+23].get_attribute("href")
			print(d)
			vt = d.find('facebook')
			link = 'https://mbasic.'+d[vt:len(d)]
			print(link)
			driver.execute_script("window.open('"+str(link)+"','_blank')")
			try:
				indexx=0
				while(indexx < len(add)):
					if(add[indexx].get_attribute("class") == 'font-bold'):
						break
					indexx += 1
				if (add[indexx+1].text.lower()== 'like'):
					driver.switch_to.window (driver.window_handles [1])
					time.sleep(random.randint(1,2))
					time.sleep(random.randint(15,20))
					driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
					time.sleep(random.randint(1,2))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[0].click()
					time.sleep(random.randint(1,2))
					try:
						j=driver.find_elements_by_tag_name("div")
						for errorfb in j :
							if(errorfb.text.lower().find("nếu bạn cho rằng nội dung này không vi phạm tiêu chuẩn cộng đồng của chúng tôi") > -1 ):
								print(errorfb.text)
								playsound("gun1.mp3",block=False)
								countfage=0
								tongsojob=0
								driver.quit()
								tang += 1
								minimain_lm_lai(index)
					except:
						time.sleep(0)
					driver.close()
					driver.switch_to.window (golike)
					time.sleep(1)
					driver.execute_script("document.getElementsByTagName('button')[2].click()")
					nuoi_fb()
					driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")
			except:
				huy_job_lm_lai()
				x+=1
			else:
				print("ngoại lệ : không biết đây là job gì ")
	except:
		driver.quit()
		tang += 1
		minimain_lm_lai(index)
	return True
def huy_job_lm_lai():
	try:
		driver.switch_to.window (driver.window_handles [1])
	except:
		return True
	driver.close()
	driver.switch_to.window (driver.window_handles [0])

def nuoi_fb():
	
	hientai =driver.current_window_handle
	driver.execute_script("window.open('https://mbasic.facebook.com/','_blank')")
	driver.switch_to.window (driver.window_handles [1]) 
	time.sleep(0.5)
	driver.execute_script("javascript:setInterval(function(){window.scrollBy(0,(Math.floor((Math.random() * 1) + 0)+1)*window.innerHeight);}, Math.floor((Math.random() * 10000) + 5000));")
	time.sleep(random.randint(10,20))
	wind = driver.window_handles
	for i in wind:
		if(i != hientai and i!= golike):
			driver.switch_to.window (i)
			driver.close()
	driver.switch_to.window (hientai)
def lam_fb_lm_lai():
	
	time.sleep(0.1)
	while (True):
		
		print("lam viec")
		if(bool(lamviec_lm_lai())==False):
			break
		
	return False


def minimain_lm_lai (x):
	#taikhoan =  ('tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13')
	taikhoan = ("tieple247",'tieple01','tieple02','tieple06','tieple07','tieple08','tieple03','tieple04','tieple05','tieple09','tieple10','tieple11','tieple12','tieple13')
	global driver,taikhoanx,tang,index,golike,countfage,tongsojob
	
	index=x
	
	while (True):
		countfage=0
		tongsojob=0
		if((index+tang*sonick) > len(taikhoan)-1):
			#tang=0
			return True
		print(index+tang*sonick)
		taikhoanx = taikhoan[index+tang*sonick]
		if os.path.exists("d:\capcha"+taikhoanx+".png"):
			os.remove("d:\capcha"+taikhoanx+".png")
		driver = initDriver(taikhoanx)
		driver.get('https://golike.mobi/jobs/facebook?tab=log')
		golike =  driver.current_window_handle
		
		chuyen=bool(lam_fb_lm_lai())
		if(chuyen == False):
			driver.quit()
			tang+=1

sonick  = 2
#def aa ():
#	Pool(sonick).map(minimain, range(0,sonick))
sojobhuy = 0 
if __name__ == '__main__':
	
	#aa()
	minimain_lm_lai(0)