from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib
import pydub
import time , os
import random
import speech_recognition as sr
import subprocess

tang=0

bi_google_chan = 0
recaptcha_button = 0

count_jobs = 0 

def delay ():
	time.sleep(random.randint(2,3) + 0.9)
def doiIPmang():
	global bi_google_chan ,recaptcha_button ,tang,index
	try:
		tx =  open(r"c:\\withpython\\trangthai.txt","r")
		if(tx.read(1)== '1' ):
			tx.close()
			print('đã được tác vụ khác chuyển IP')
			return True
		else:
			tx.close()
			tx =  open(r"c:\\withpython\\trangthai.txt","w")
			tx.write('1')
			tx.close()
			subprocess.call('python doi-ip-mang.py')
			tx =  open(r"c:\\withpython\\trangthai.txt","w")
			tx.write('0')
			tx.close()
			time.sleep(2)
	except:
		print('bug')
	bi_google_chan = 0
	recaptcha_button = 0
	danh_dau_ket_thuc_doc_file(taikhoanx)
	driver.quit()
	tang += 1
	minimain(index)
def giaicaptchagg(i):
	global recaptcha_button
	driver.switch_to.default_content()
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[i])
	delay()
	try:
		driver.find_element_by_tag_name("button").click() #play -----------------------------
		delay()

		src = driver.find_element_by_id("audio-source").get_attribute("src")
		
		urllib.request.urlretrieve(src, "C:\\withpython\\sample"+str(taikhoanx)+".mp3")
		sound = pydub.AudioSegment.from_mp3("c:\\withpython\\sample"+str(taikhoanx)+".mp3")
		sound.export("C:\\withpython\\sample"+str(taikhoanx)+".wav", format="wav")
		sample_audio = sr.AudioFile("C:\\withpython\\sample"+str(taikhoanx)+".wav")
		
		r = sr.Recognizer()
		with sample_audio as source:
			audio = r.record(source)
		key = r.recognize_google(audio)
		
		if os.path.exists("C:\\withpython\\sample"+str(taikhoanx)+".wav"):
			os.remove("C:\\withpython\\sample"+str(taikhoanx)+".wav")
		if os.path.exists("C:\\withpython\\sample"+str(taikhoanx)+".mp3"):
			os.remove("C:\\withpython\\sample"+str(taikhoanx)+".mp3")
		delay()

		driver.find_element_by_id("audio-response").send_keys(key.lower())
		delay()
		driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
		delay()
		
		try:
			if(driver.find_element_by_class_name("rc-doscaptcha-header-text").text == 'Try again later'):
				driver.refresh()
				lamtiep()
				return True
		except:pass
		try:
			if(driver.find_element_by_class_name("rc-audiochallenge-error-message").text == 'Multiple correct solutions required - please solve more.'):
				giaicaptchagg(i)
				return True
		except:pass
	except:
		print("recaptcha-reload-button")
		recaptcha_button += 1
		if(recaptcha_button > 3):
			print("đổi IP mạng > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > ")
			doiIPmang()
			sleep1()
		driver.refresh()
		lamtiep()
		return True
	delay()
	
def lamtiep():
	doi_load()
	try:
		for i in range(0,3):
			if(driver.execute_script('return document.getElementsByClassName("btn bg-button-1 px-0 btn-block")['+str(i)+'].innerText') == "TikTok"):
				driver.execute_script("document.getElementsByClassName('btn bg-button-1 px-0 btn-block')[0].href ='file:///C:/Users/tiepl/Desktop/web.html'")
				break
	except:
		return True
	driver.find_element_by_link_text('TikTok').click()

	doi_load()
	for i in driver.find_elements_by_tag_name('button'):
		#print(i.text)
		if(i.text.find('oàn') != -1):
			#print('ok')
			i.click()
			break
	xetcapcha()
def captchagg():
	global bi_google_chan
	driver.switch_to.default_content()
	doi_captcha()
	try:
		for i in range(0,len(driver.find_elements_by_tag_name("iframe"))):
			if(driver.find_elements_by_tag_name("iframe")[i].find_element_by_xpath("..").find_element_by_xpath("..").get_attribute("style").find("visibility: visible;") != -1):
				driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[i])
				delay()
				#chuyen sang captcha am thanh
				driver.find_element_by_id("recaptcha-audio-button").click()
				delay()
				bi_google_chan = 0
				
				giaicaptchagg(i)
				
				break

	except:
		print("mã lỗi 137")
		bi_google_chan += 1
		if(bi_google_chan > 1):
			print("đổi IP mạng > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > ")
			doiIPmang()
	driver.switch_to.default_content()

def danh_dau_ket_thuc_doc_file(name_file):
	file_is_reading = open(r"c:\\withpython\\jobs_tiktok\\account-what-is-reading.txt","r")
	f_reading = file_is_reading.readlines()
	file_is_reading.close()

	file_is_reading = open(r"c:\\withpython\\jobs_tiktok\\account-what-is-reading.txt","w")
	for xet in f_reading:
		if(xet.find(name_file) != -1 ):
			f_reading.remove(xet)
	file_is_reading.writelines(f_reading)
	file_is_reading.close()

def danh_dau_bat_dau_doc_file(namefile):
	file_is_reading = open(r"c:\\withpython\\jobs_tiktok\\account-what-is-reading.txt","a")
	file_is_reading.write(namefile)
	file_is_reading.write('\n')
	file_is_reading.close()

def xin_ghi_file (namefile):
	file_is_reading = open(r"c:\\withpython\\jobs_tiktok\\account-what-is-reading.txt","r")
	f_reading = file_is_reading.readlines()
	file_is_reading.close()

	for r in f_reading:
		if( r.find(namefile) != -1):
			return False
	return True

def initDriver(filepath):
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\\withpython\\account_tiktok_to_crawl_jobs\\'+ filepath) 

	options.add_argument("--disable-blink-features")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	
	options.headless = True
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	
	driver = webdriver.Chrome(executable_path=r'c:\\withpython\\chromedriver.exe', options=options)
	driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"})
	return driver
	

def lay_jobs():
	try:
		if(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text == 'Chi tiết'):return False
		elif(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text == 'Kiếm tiền'):pass
		else:
			sleep1()
			driver.execute_script("document.getElementsByClassName('font-20 d-block mb-1 icon-wallet')[0].click()")
			sleep1()
			driver.execute_script("document.getElementsByClassName('btn btn-outline-light')[2].click()")
		sleep1()
		if(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text == 'Chi tiết'):return False
		driver.execute_script("document.getElementsByClassName('btn btn-outline-light')[0].click()")
		return True
	except:
		return False
def sleep1():
	time.sleep(random.randint(1,2))

def doi_load():
	try:
		while(driver.find_elements_by_tag_name("img")[7].get_attribute("style") == 'width: 19px; display: none;'):
			pass
	except:
		return True
def doi_captcha():
	try:
		if(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.ID, "toast-container")))
		#print("doi-xong")
	except:
		pass
def xetcapcha():
	
	global tang,golike,bi_google_chan,recaptcha_button,taikhoanx,count_jobs
	
	doi_captcha()
	captchagg()

	try:
		if(driver.find_element_by_id('swal2-content').get_attribute("style") != "display: block;"):
			return True
		cten = driver.find_element_by_id('swal2-content')
		try:
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
		except:
			pass
		
		if(cten.text.find('thành công') != -1 ):
			count_jobs += 1
			if(count_jobs > 10):
				print('du 10 jobs -----------------------------------------------------')
				danh_dau_ket_thuc_doc_file(taikhoanx)
				driver.quit()
				tang += 1
				minimain(index)
		if(cten.text.find('quá') != -1 and cten.text.find('jobs') != -1 ):
			print("=============================Bạn đã làm quá 150 jobs ============================")
			danh_dau_ket_thuc_doc_file(taikhoanx)
			driver.quit()
			tang += 1
			minimain(index)
	except:
		return True

def sleep13():
	time.sleep( random.randint(55,75)/10 )
def sleep06():
	time.sleep( random.randint(10,12)/10 )

def lamviec():
	global document,bi_google_chan,recaptcha_button 
	
	try:
		solankhongload = 0
		while(lay_jobs()==True):
			solankhongload += 1
			if(solankhongload > 10):
				doiIPmang()
				return False
			xetcapcha()
			pass
		solankhongload = 0
		doi_load()
		try:
			for i in range(0,3):
				if(driver.execute_script('return document.getElementsByClassName("btn bg-button-1 px-0 btn-block")['+str(i)+'].innerText') == "TikTok"):
					url = driver.execute_script("return document.getElementsByClassName('btn bg-button-1 px-0 btn-block')[0].href")
					driver.execute_script("document.getElementsByClassName('btn bg-button-1 px-0 btn-block')[0].href ='file:///C:/Users/tiepl/Desktop/web.html'")
					break
		except:
			return True
		driver.find_element_by_link_text('TikTok').click()
		print(url)
		f = open('c:\\withpython\\jobs_tiktok\\'+str(taikhoanx)+'.txt','a')
		f.write(url)
		f.write("\n")
		f.close()
		bi_google_chan = 0
		recaptcha_button = 0

		doi_load()
		for i in driver.find_elements_by_tag_name('button'):
			#print(i.text)
			if(i.text.find('oàn') != -1):
				#print('ok')
				i.click()
				break
		xetcapcha()
		return True
	except:
		return True
def lam_tiktok():
	while (True):
		if(bool(lamviec())==False):
			break
	return False


def minimain (x):
	#taikhoan =  ('tieple247','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
	taikhoan =  ('tieple247','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17','tieple19',"tieple20",'tieple21','letiep1','letiep3','letiep4','letiep5','letiep6','letiep7','letiep8')
	global driver,taikhoanx,tang,index,golike
	
	index=x
	
	while (True):
		if((index+tang) > len(taikhoan)-1):
			tang=0
			#minimain_lm_lai(index)
			
		taikhoanx = taikhoan[index+tang]
		print(taikhoanx)
		while( not xin_ghi_file(taikhoanx) ):
			tang += 1
			if((index+tang) > len(taikhoan)-1):
				tang=0
			taikhoanx = taikhoan[index+tang]
			print(taikhoanx)
		danh_dau_bat_dau_doc_file(taikhoanx)
		driver = initDriver(taikhoanx)
		
		
		time.sleep(1)
		driver.get("https://golike.mobi/home")
		chuyen=bool(lam_tiktok())
		
		if(chuyen == False):
			danh_dau_ket_thuc_doc_file(taikhoanx)
			driver.quit()
			tang+=1



if __name__ == '__main__':
	minimain(0)