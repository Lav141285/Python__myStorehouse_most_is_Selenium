from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool
from datetime import datetime
from urllib.request import urlretrieve
import pydub
import time , os
import random,docx
import speech_recognition as sr
import subprocess,threading

class CAPTCHA:pass
'''
	def doi_captcha(self):
		if(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		try:
			WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.ID, "toast-container")))
			#print("doi-xong")
		except:
			pass
	def xetcapcha(self):
		
		global tang,golike,tongsojob,countfage,sojobhuy,bi_google_chan,recaptcha_button
		driver.switch_to.window (driver.window_handles [0])
		doi_captcha()
		captchagg()
		
		try:
			if(driver.find_element_by_id('swal2-content').get_attribute("style") != "display: block;"):
				return True
			cten = driver.find_element_by_id('swal2-content')
			
			try:
				WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]")))
				try:
					driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				except:
					pass
				return True
			except:
				pass
			if(cten.text.find('Hệ thống jobs đang trong quá trình xử lý chặn auto và phân phối jobs') != -1):
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok

				return True
			elif(cten.text.find('Không tải được danh sách Job do tài khoản Facebook bị khóa. Nếu tài khoản không bị khóa hãy vào menu tài khoản và Cập nhật lại thông tin tài khoản.') != -1 ):
				driver.get("https://golike.mobi/account/manager/facebook")
				sleep13()
				driver.execute_script("document.getElementsByClassName('material-icons float-right d200 hand')[0].click()")
				time.sleep(1)
				driver.execute_script("document.getElementsByClassName('d-block')[9].click()")
				sleep13()
				lay_jobs()
				return True
			if(cten.text.find('Đã gửi thông tin lên hệ thống xét duyệt') != -1 ):
				print(cten.text[(len(cten.text)-3):len(cten.text)])
				tongsojob +=1
				sojobhuy = 0
				bi_google_chan = 0
				recaptcha_button = 0
				nuoi_fb()
				if(tongsojob > sojob ):
					print("=============================đủ ",sojob,"============================")
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
			if ( cten.text.find('Không thể báo cáo hoàn thành lại do đã hết') != -1 ):
				print(cten.text)
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				
				doi_load()
				return False
			if(cten.text.find('Để đảm bảo công bằng cho mọi người') != -1 and sonick > 2):
				print("đổi IP mạng > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > ")
				doiIPmang()
				driver.quit()
				print("chỉ được dùng 2 fb trên 1 ip mạng ------------------------------------------------------------------------------")
				input()
			if(cten.text.find('Hệ thống đang tự động phân phối tối ưu jobs') != -1 or cten.text.find('timeout of 0ms exceeded') != -1 ):
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				time.sleep(60)
				
				return True
			if(  cten.text.find('Tài khoản của bạn KHÔNG sẵn sàng làm jobs like page') != -1  or cten.text.find('Đã gửi báo cáo lên hệ thống') != -1   ):
				
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				return True

			if(cten.text.find('Bạn chưa làm việc, không thể bấm hoàn thành') != -1 or cten.text.find('Bài viết đã đủ số lượng') != -1  or cten.text.find('Bài viết này đã bị ẩn khi bị mọi người báo cáo lỗi quá nhiều') != -1 or cten.text.find('Không thể báo cáo hoàn thành do bạn đã làm công việc này rồi') != -1 ):
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				to_cao(3)
				return True
			if(cten.text.find('Vui lòng cập nhật phiên bản mới nhất để làm việc') != -1 or cten.text.find('thử lại sau ít phút') != -1 or cten.text.find('Thao tác quá nhanh vui lòng làm chậm lại 1 xíu nhé bạn !') != -1  or cten.text.find('Error') != -1 or cten.text.find('quá nhanh') != -1):
				lamtiep()
				return True
			if(cten.text.find('chưa thực hiện thao tác') != -1 or cten.text.find(' hết hạn hoàn thành') != -1 ):
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				to_cao(2)
				return True
			if(cten.text.find('quá 100 jobs') != -1 or cten.text.find('ghỉ ngơi để đảm bảo sức khỏe và quay lại vào ngày mai để làm việc tiếp nhé') != -1 or cten.text.find('Bạn đã nhập sai câu hỏi xác nhận quá 3 lần') != -1):
				print("=============================Bạn đã làm quá 100 jobs ============================")
				countfage=0
				tongsojob=0
				driver.quit()
				tang += 1
				minimain(index)
			if(cten.text.find('hoàn thành lại thành công') != -1 ):
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				return True
			else:
				print(cten.text)
				lay_jobs()
				#playsound("C:\withpython\gun0.mp3",block=False)
				
		except:
			return True

	def delay (self):
		time.sleep(random.randint(2,3) + 0.9)
	def doiIPmang(self):
		
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
		self.bi_google_chan = 0
		self.recaptcha_button = 0
		
	def giaicaptchagg(self,i):
		
		self.driver.switch_to.default_content()
		if(self.driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[i])
		self.delay()
		try:
			self.driver.find_element_by_tag_name("button").click() #play -----------------------------
			self.delay()

			#get the mp3 audio file
			src = self.driver.find_element_by_id("audio-source").get_attribute("src")
			#print("[INFO] Audio src: %s"%src)
			#download the mp3 audio file from the source
			urlretrieve(src, "C:\\withpython\\sample"+str(taikhoanx)+".mp3")
			sound = pydub.AudioSegment.from_mp3("c:\\withpython\\sample"+str(taikhoanx)+".mp3")
			sound.export("C:\\withpython\\sample"+str(taikhoanx)+".wav", format="wav")
			sample_audio = sr.AudioFile("C:\\withpython\\sample"+str(taikhoanx)+".wav")
			print('[+] Audio Saved')
			r = sr.Recognizer()
			with sample_audio as source:
				audio = r.record(source)
			key = r.recognize_google(audio)
			print('[INFO] Recaptcha Passcode:',key)
			if os.path.exists("C:\\withpython\\sample"+str(taikhoanx)+".wav"):
				os.remove("C:\\withpython\\sample"+str(taikhoanx)+".wav")
			if os.path.exists("C:\\withpython\\sample"+str(taikhoanx)+".mp3"):
				os.remove("C:\\withpython\\sample"+str(taikhoanx)+".mp3")
			delay()
			#key in results and submit
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
		
	def lamtiep(self):
		if(driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		tim=0
		sleep1()
		try:
			mbasic1= driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower().find("mb") > -1):
					
					driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					
					tim=1
					break
				dem+=1
			if(tim == 0):
				print("không có mbasic")
				driver.execute_script("document.getElementsByTagName('h6')[2].click()")
				
		except:
			print("không nhấn mbasic")
			return True
		doi_load()
		sleep13()
		try:
			self.driver.switch_to.window (self.driver.window_handles [1])
			self.driver.close()
		except:
			print("lỗi tắt tab---------------------------------------------------------------------")
			lay_jobs()
			return True
		self.driver.switch_to.window (self.driver.window_handles [0])
		#nhấn hoàn thành 
		try:
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower() == "hoàn thành"):
					driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					tim=1
					break
				dem+=1
		except:
			print("-----------------------------------------------------------------------------")
		
		self.captchagg()
	def captchagg(self):
		global bi_google_chan
		if(self.driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		self.driver.switch_to.default_content()
		self.doi_captcha()
		try:
			for i in range(0,len(self.driver.find_elements_by_tag_name("iframe"))):
				if(self.driver.find_elements_by_tag_name("iframe")[i].find_element_by_xpath("..").find_element_by_xpath("..").get_attribute("style").find("visibility: visible;") != -1):
					self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[i])
					self.delay()
					#r = random.randint(0,4)
					#if(r==0):
					#	driver.execute_script("document.getElementsByTagName('td')["+str(random.randint(0,8))+"].click()")
					self.delay()#chuyen sang captcha am thanh
					self.driver.find_element_by_id("recaptcha-audio-button").click()
					self.delay()
					bi_google_chan = 0
					#---------------------------------------------------
					self.giaicaptchagg(i)
					#---------------------------------------------------
					#driver.find_element_by_id("recaptcha-verify-button").click()
					break
			#print("vượt captcha thành công")
		except:
			print("mã lỗi 137")
			bi_google_chan += 1
			if(bi_google_chan > 1):
				print("đổi IP mạng > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > ")
				self.doiIPmang()
		self.driver.switch_to.default_content()
'''
class DRIVER:
	taikhoan =  ('tieple247','tieple01','tieple03','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple16','tieple17','tieple19',"tieple20",'tieple21','letiep1','letiep3','letiep5','letiep6','letiep7','letiep8')
	stt = 0
	driver = None
	def __init__(self):
		options = webdriver.ChromeOptions()
		options.add_argument(r'user-data-dir=c:\\withpython\\account_facebook\\'+ self.taikhoan[self.stt])
		options.add_argument("start-maximized")
		options.add_experimental_option("excludeSwitches", ["enable-automation"])
		options.add_experimental_option('useAutomationExtension', False)
		options.add_argument("--disable-blink-features")
		options.add_argument("--disable-blink-features=AutomationControlled")
		#options.headless = True
		prefs = {
		"profile.managed_default_content_settings.images": 1
		}
		options.add_experimental_option("prefs", prefs)
		
		self.driver = webdriver.Chrome(executable_path=r'c:\\withpython\\chromedriver.exe', options=options)
		self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"})
		if(DRIVER.stt == len(self.taikhoan) - 1):
			DRIVER.stt = 0
		else:DRIVER.stt +=1


class LAM_FB:
	pass
class LAM_GOLIKE(CAPTCHA):
	sojob = 100
	countfage=0
	tongsojob=0
	driver = None
	def __init__(self,driver_join):
		self.driver=driver_join
	def sleep13(self):
		time.sleep( random.randint(55,75)/10 )
	def doi_load(self):
		try:
			while(self.driver.find_elements_by_tag_name("img")[6].get_attribute("style") == 'display: none;'):
				pass
		except:
			return True
	def to_cao(self,tc):
		
		self.doi_load()
		if(self.driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		try:
			self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
		except:
			pass
		print("đang tố cáo")
		time.sleep(5)
		self.sojobhuy += 1
		try:
		#nhấn báo lỗi
			tocao= self.driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in tocao:
				if(mb1.text.lower() == "báo lỗi"):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					break
				dem+=1
		#Tôi không muốn làm Job này
			time.sleep(3)
			if(tc == 0):
				dem=0
				for mb1 in tocao:
					if(mb1.text == "Tôi không muốn làm Job này"):
						self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
						break
					dem+=1
			elif(tc == 1):
				dem=0
				for mb1 in tocao:
					if(mb1.text == "Tôi đã làm Job này rồi"):
						self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
						break
					dem+=1
			elif(tc == 2):
				dem=0
				for mb1 in tocao:
					if(mb1.text == "Báo cáo hoàn thành thất bại"):
						self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
						break
					dem+=1
			elif(tc == 3):
				dem=0
				for mb1 in tocao:
					if(mb1.text == "Job đủ số lượng"):
						self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
						break
					dem+=1     
		#nhấn gửi 
			self.driver.execute_script("document.getElementsByClassName('btn btn-primary btn-sm form-control mt-3')[0].click()")
		except:
			return True
		
		self.doi_load()
		xetcapcha()
	def huy_job(self):
		try:
			self.driver.switch_to.window (self.driver.window_handles [1])
		except:
			return True
		self.driver.close()
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		self.doi_load()
		self.xetcapcha()
		self.doi_load()
		print("huy job")
		self.to_cao(0)
		self.doi_load()
		self.xetcapcha()
		self.doi_load()
	def like_fage(self):
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		tim=0
		try:
			mbasic1= self.driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower().find("mb") > -1):
					
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					loai = 1 
					tim=1
					break
				dem+=1
			if(tim == 0):
				print("không có mbasic")
				self.driver.execute_script("document.getElementsByTagName('h6')[2].click()")
				loai=2
		except:
			print("không nhấn mbasic")				
			self.to_cao(0)
			return True

		self.driver.switch_to.window (self.driver.window_handles [1])
		#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
		if(sojobhuy > 1):
			inputdangnhap = self.driver.find_elements_by_tag_name("input")
			
			for ip in inputdangnhap :
				#print(ip.get_attribute("value").lower())
				if (ip.get_attribute("value").lower() == "đăng nhập"):
					f = open('C:\\withpython\\tk_bi_dang_xuat.txt','a')
					f.write("\n\n\n")
					f.write("day ")
					f.write(str(datetime.now().day))
					f.write(" month ")
					f.write(str(datetime.now().month))
					f.write(" year ")
					f.write(str(datetime.now().year))
					f.write(" when ")
					f.write(str(datetime.now().hour))
					f.write("hour")
					f.write(str(datetime.now().minute))
					f.write("minute")
					f.write(str(datetime.now().second))
					f.write("second")
					f.write("\n")
					f.write(self.taikhoanx)
					f.close()
					'''
					print("=============================CHUYỂN NICK DO BỊ ĐĂNG XUẤT ============================")
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					self.minimain(index)
					'''
					ip.click()
					time.sleep(2)
					self.driver.refresh()
			time.sleep(0.1)
		
		try:
			if(loai == 1 ):
				#while(driver.find_element_by_id("pages_follow_action_id").get_attribute("href") == None):
				#	pass
				#if(driver.find_element_by_id("pages_follow_action_id").get_attribute("href").find("subscriptions") != -1):
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(random.randint(0,1))
				self.driver.execute_script("window.scrollTo(0, 0);")
				self.driver.execute_script("document.getElementsByClassName('ct')[0].click()")#nhanlikefage
				time.sleep(random.randint(0,1))
				#else:print("loi ",".",driver.find_element_by_id("pages_follow_action_id").get_attribute("href"))
			if(loai == 2):
				d = self.driver.current_url
				vt = d.find('facebook')
				self.driver.get('https://mbasic.'+d[vt:len(d)])
				#while(driver.find_element_by_id("pages_follow_action_id").get_attribute("href") == None):
				#	pass
				#if(driver.find_element_by_id("pages_follow_action_id").get_attribute("href").find("subscriptions") != -1):
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				time.sleep(random.randint(0,1))
				self.driver.execute_script("window.scrollTo(0, 0);")
				time.sleep(random.randint(0,1))
				self.driver.execute_script("document.getElementsByClassName('ct')[0].click()")#nhanlikefage
				time.sleep(random.randint(0,1))
				#else:print("loi ",".",driver.find_element_by_id("pages_follow_action_id").get_attribute("href"))
			self.sleep13()
			self.driver.close()
			self.driver.switch_to.window (self.driver.window_handles [0])
			
			self.doi_load()
		
			xetcapcha()
			
			self.doi_load()
			#nhấn hoàn thành 
			
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,2))
			self.driver.execute_script("window.scrollTo(0, 0);")
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower() == "hoàn thành"):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					tim=1
					break
				dem+=1
			if(tim == 0):
				return True
			
		except:
			self.huy_job()
			return True
		
		self.doi_load()
		
		self.xetcapcha()
		self.doi_load()
		
		self.countfage+=1
		return True
	def theo_doi(self):
		self.driver.switch_to.window (self.driver.window_handles [0])
		tim=0
		try:
			mbasic1= self.driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower().find("mb") > -1):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					loai=1
					tim=1
					break
				dem+=1
			if(tim == 0):
				print("không có mbasic")
				self.driver.execute_script("document.getElementsByTagName('h6')[2].click()")
				loai=2
		except:
			
			return True
		time.sleep(0.1)
		self.driver.switch_to.window (self.driver.window_handles [1])
		#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
		if(sojobhuy > 1):
			inputdangnhap = self.driver.find_elements_by_tag_name("input")
			
			for ip in inputdangnhap :
				#print(ip.get_attribute("value").lower())
				if (ip.get_attribute("value").lower() == "đăng nhập"):
					f = open('C:\\withpython\\tk_bi_dang_xuat.txt','a')
					f.write("\n\n\n")
					f.write("day ")
					f.write(str(datetime.now().day))
					f.write(" month ")
					f.write(str(datetime.now().month))
					f.write(" year ")
					f.write(str(datetime.now().year))
					f.write(" when ")
					f.write(str(datetime.now().hour))
					f.write("hour")
					f.write(str(datetime.now().minute))
					f.write("minute")
					f.write(str(datetime.now().second))
					f.write("second")
					f.write("\n")
					f.write(self.taikhoanx)
					f.close()
					'''
					print("=============================CHUYỂN NICK do bi dang xuat ============================")
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
					'''
					ip.click()
					time.sleep(2)
					self.driver.refresh()
		
		#nhấn theo dõi
		try:
			if(loai == 1):
				time.sleep(random.randint(0,1))
				self.driver.find_element_by_link_text("Theo dõi").click()
				time.sleep(random.randint(0,1))
			if(loai == 2):
				
				d = self.driver.current_url
				vt = d.find('facebook')
				self.driver.get('https://mbasic.'+d[vt:len(d)])
				time.sleep(random.randint(0,1))
				self.driver.find_element_by_link_text("Theo dõi").click()
				time.sleep(random.randint(0,1))
		except:
			pass
		self.sleep13()
		self.driver.switch_to.window (self.driver.window_handles [1])
		self.driver.close()
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		self.doi_load()
		self.xetcapcha()
		self.doi_load()
		
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(random.randint(1,2))
		self.driver.execute_script("window.scrollTo(0, 0);")
		dem=0
		for mb1 in mbasic1:
			if(mb1.text.lower() == "hoàn thành"):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			
			return True
		
		self.doi_load()
		
		self.xetcapcha() 
		self.doi_load()
		
		return True	

	def xet_cai_nao_da_an(self):
		try:
			if(self.driver.find_element_by_link_text("Thích").get_attribute("class") != ""):
				return 0
		except:pass
		try:
			if(self.driver.find_element_by_link_text("Yêu thích").get_attribute("class") != ""):
				return 1
		except:pass
		try:
			if(self.driver.find_element_by_link_text("Thương thương").get_attribute("class") != ""):
				return 2
		except:pass
		try:
			if(self.driver.find_element_by_link_text("Haha").get_attribute("class") != ""):
				return 3
		except:pass
		try:
			if(self.driver.find_element_by_link_text("Wow").get_attribute("class") != ""):
				return 4
		except:pass
		try:
			if(self.driver.find_element_by_link_text("Buồn").get_attribute("class") != ""):
				return 5
		except:pass
		#if(driver.find_element_by_link_text("Phẫn nộ").get_attribute("class") != ""):
		return 6
	def nhanbaytocamxuc(self,abc):
		try:
			if(self.driver.find_element_by_link_text("Bày tỏ cảm xúc").get_attribute("class") == ""):
				dk=True
			else:
				dk=False
		except:
			dk=True
		if (dk):#đã nhấn bay to cam xuc
			cai_nao_da_an = self.xet_cai_nao_da_an()
			if(cai_nao_da_an == 0):#đã nhấn like
				if(abc == 0):#cần nhấn like
					return True
				else:#không cần nhấn like
					'''
					driver.find_element_by_link_text("Thích").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 1):#đã nhấn Yêu thích
				if(abc == 1):#cần nhấn Yêu thích
					return True
				else:#không cần nhấn Yêu thích
					'''
					driver.find_element_by_link_text("Yêu thích").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 2):#đã nhấn Thương thương
				if(abc == 2):#cần nhấn Thương thương
					return True
				else:#không cần nhấn Thương thương
					'''
					driver.find_element_by_link_text("Thương thương").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 3):#đã nhấn Haha
				if(abc == 3):#cần nhấn Haha
					return True
				else:#không cần nhấn Haha
					'''
					driver.find_element_by_link_text("Haha").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 4):#đã nhấn Wow
				if(abc == 4):#cần nhấn Wow
					return True
				else:#không cần nhấn Wow
					'''
					driver.find_element_by_link_text("Wow").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 5):#đã nhấn Buồn
				if(abc == 5):#cần nhấn Buồn
					return True
				else:#không cần nhấn Buồn
					'''
					driver.find_element_by_link_text("Buồn").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False
			elif(cai_nao_da_an == 6):#đã nhấn Phẫn nộ
				if(abc == 6):#cần nhấn Phẫn nộ
					return True
				else:#không cần nhấn Phẫn nộ
					'''
					driver.find_element_by_link_text("Phẫn nộ").click()
					time.sleep(random.randint(0,1))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[abc].click()
					'''
					self.to_cao(1)
					return False	
		else:#nếu chưa nhấn
			time.sleep(random.randint(0,1))
			self.driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(0,1))
			nhan=self.driver.find_elements_by_tag_name('li')
			nhan[abc].click()
			return True
	def baytocamxuc(self,abc):
		self.driver.switch_to.window (self.driver.window_handles [0])
		tim=0
		try:
			mbasic1= self.driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in mbasic1:
				
				if(mb1.text.lower().find("mb") > -1):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					loai =1
					tim=1
					break
				dem+=1
			if(tim == 0):
				print("không có mbasic")
				self.driver.execute_script("document.getElementsByTagName('h6')[2].click()")
				loai=2
		except:
			
			return True


		self.driver.switch_to.window (self.driver.window_handles [1])

		#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
		if(sojobhuy > 1):
			inputdangnhap = self.driver.find_elements_by_tag_name("input")
			
			for ip in inputdangnhap :
				#print(ip.get_attribute("value").lower())
				if (ip.get_attribute("value").lower() == "đăng nhập"):
					f = open('C:\\withpython\\tk_bi_dang_xuat.txt','a')
					f.write("\n\n\n")
					f.write("day ")
					f.write(str(datetime.now().day))
					f.write(" month ")
					f.write(str(datetime.now().month))
					f.write(" year ")
					f.write(str(datetime.now().year))
					f.write(" when ")
					f.write(str(datetime.now().hour))
					f.write("hour")
					f.write(str(datetime.now().minute))
					f.write("minute")
					f.write(str(datetime.now().second))
					f.write("second")
					f.write("\n")
					f.write(self.taikhoanx)
					f.close()
					'''
					print("=============================CHUYỂN NICK DO BỊ ĐĂNG XUẤT ============================")
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
					'''
					ip.click()
					time.sleep(2)
					self.driver.refresh()
			time.sleep(0.1)

		try:
			if(loai == 1):
				if(not self.nhanbaytocamxuc(abc)):
					return True
				time.sleep(random.randint(0,1))
			if(loai == 2):
				d = self.driver.current_url
				vt = d.find('facebook')
				self.driver.get('https://mbasic.'+d[vt:len(d)])
				if(not self.nhanbaytocamxuc(abc)):
					return True
				time.sleep(random.randint(0,1))
			if(sojobhuy > 1):
				try:
					j=self.driver.find_elements_by_tag_name("div")
					for i in j :
						if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
							print(i.text)
							f = open('C:\\withpython\\tk_bi_chan.txt','a')
							f.write("\n\n\n")
							f.write("day ")
							f.write(str(datetime.now().day))
							f.write(" month ")
							f.write(str(datetime.now().month))
							f.write(" year ")
							f.write(str(datetime.now().year))
							f.write(" when ")
							f.write(str(datetime.now().hour))
							f.write("hour")
							f.write(str(datetime.now().minute))
							f.write("minute")
							f.write(str(datetime.now().second))
							f.write("second")
							f.write("\n")
							f.write(self.taikhoanx)
							f.write("\n")
							
							f.close()
							playsound("C:\withpython\gun1.mp3",block=False)
							countfage=0
							tongsojob=0
							self.driver.quit()
							self.tang += 1
							self.minimain(self.index)
				except:
					pass
			self.sleep13()
			self.driver.switch_to.window (self.driver.window_handles [1])
			self.driver.close()
			self.driver.switch_to.window (self.driver.window_handles [0])
			
			self.doi_load()
			xetcapcha()
			self.doi_load()
			
			self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,2))
			self.driver.execute_script("window.scrollTo(0, 0);")
			dem=0
			for mb1 in mbasic1:
				if(mb1.text.lower() == "hoàn thành"):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					tim=1
					break
				dem+=1
			if(tim == 0):
				
				return True
			
			self.doi_load()
			
			self.xetcapcha()
			self.doi_load()
			
		except:
			self.huy_job()
		self.doi_load()
		self.xetcapcha()
		
		self.doi_load()
		return True

	def tang_comment(self):
		
		self.driver.switch_to.window (self.driver.window_handles [0])
		try:
			self.driver.execute_script("document.getElementsByTagName('u')[0].click()")#nhan copy
			self.driver.execute_script("document.getElementsByTagName('u')[0].click()")#nhan copy
		except:
			pass
		
		comment = self.driver.find_elements_by_tag_name("span")[7].text
		mbasic= self.driver.find_elements_by_tag_name("h6")
		dem=0
		for mb in mbasic:
			if(mb.text.lower().find("mb") > -1):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				break
			dem+=1
		self.driver.switch_to.window (self.driver.window_handles [1])
		if(sojobhuy > 1):
			inputdangnhap = self.driver.find_elements_by_tag_name("input")

			for ip in inputdangnhap :
				#print(ip.get_attribute("value").lower())
				if (ip.get_attribute("value").lower() == "đăng nhập"):
					f = open('C:\\withpython\\tk_bi_dang_xuat.txt','a')
					f.write("\n\n\n")
					f.write("day ")
					f.write(str(datetime.now().day))
					f.write(" month ")
					f.write(str(datetime.now().month))
					f.write(" year ")
					f.write(str(datetime.now().year))
					f.write(" when ")
					f.write(str(datetime.now().hour))
					f.write("hour")
					f.write(str(datetime.now().minute))
					f.write("minute")
					f.write(str(datetime.now().second))
					f.write("second")
					f.write("\n")
					f.write(self.taikhoanx)
					f.close()
					'''
					print("=============================CHUYỂN NICK DO BỊ ĐĂNG XUẤT ============================")
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
					'''
					ip.click()
					time.sleep(2)
					self.driver.refresh()
		try:
			time.sleep(random.randint(0,1))
			self.driver.find_element_by_name("comment_text").send_keys(comment)
			time.sleep(random.randint(0,1))
			inp = self.driver.find_elements_by_tag_name("input")
			time.sleep(1)
			for ip in inp :
				if(ip.get_attribute("value")== 'Bình luận'):
					ip.click()
					break
			time.sleep(random.randint(0,1))
			self.sleep13()
			self.driver.close()
		except:
			print("khong binh luan duoc")
			pass
		self.driver.switch_to.window (self.driver.window_handles [0])
		time.sleep(0.1)
		
		print("mbasic",len(mbasic))
		
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(random.randint(1,2))
		self.driver.execute_script("window.scrollTo(0, 0);")
		dem=0
		for mb1 in mbasic:
			if(mb1.text.lower() == "hoàn thành"):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			
			return True
		self.doi_load()
		self.xetcapcha()
		self.doi_load()
		self.xetcapcha()
		self.doi_load()
		return True
	def like_comment(self,abc):
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		try:
			mbasic1= self.driver.find_elements_by_tag_name("h6")
			dem=0
			for mb1 in mbasic1:
				
				if(mb1.text.lower().find("mb") > -1):
					self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
					
					
					break
				dem+=1
		except:
			
			return True

		
		self.driver.switch_to.window (self.driver.window_handles [1])
		
		time.sleep(random.randint(0,1))
		nhan=self.driver.find_elements_by_tag_name('li')
		nhan[abc].click()
		time.sleep(random.randint(0,1))
		self.sleep13()
		self.driver.switch_to.window (self.driver.window_handles [1])
		self.driver.close()
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		self.doi_load()
		xetcapcha()
		self.doi_load()
		
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(random.randint(1,2))
		self.driver.execute_script("window.scrollTo(0, 0);")
		dem=0
		for mb1 in mbasic1:
			if(mb1.text.lower() == "hoàn thành"):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			
			return True
			
		self.doi_load()
		
		xetcapcha()
		self.doi_load()
		return True
	def chiase(self):
		self.driver.execute_script("document.getElementsByTagName('u')[0].click()")
		self.doi_load()
		mbasic1= self.driver.find_elements_by_tag_name("h6")
		dem =0
		tim=0
		for mb1 in mbasic1:
			if(mb1.text == "Làm việc bằng ứng dụng Facebook trên điện thoại."):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		dem =0
		self.driver.switch_to.window (self.driver.window_handles [1])
		time.sleep(random.randint(0,1))
		self.driver.find_element_by_link_text("Chia sẻ").click()
		time.sleep(random.randint(0,1))
		self.driver.execute_script("document.getElementsByClassName('bh cq cr cs ct')[0].click()")
		time.sleep(random.randint(0,1))
		self.driver.switch_to.window (self.driver.window_handles [0])
		self.doi_load()
		tim =0
		for mb1 in mbasic1:
			if(mb1.text == "Kiểm tra bằng trình duyệt Web trên điện thoại."):
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		dem =0
		self.sleep13()
		self.driver.switch_to.window (self.driver.window_handles [1])
		self.driver.close()
		self.driver.switch_to.window (self.driver.window_handles [0])
		
		self.doi_load()
		
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(random.randint(1,2))
		self.driver.execute_script("window.scrollTo(0, 0);")
		tim =0
		for mb1 in mbasic1:
			if(mb1.text.lower() == "hoàn thành"):
				self.driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			
			return True	
		self.doi_load()
		
		self.xetcapcha()
		self.doi_load()
		return True
	def doi_captcha(self):
		if(self.driver.execute_script("return document.getElementsByClassName('b200 maintenance text-white')")[0].text != "Chi tiết"):
			return True
		try:
			WebDriverWait(self.driver, 1.5).until(EC.presence_of_element_located((By.ID, "toast-container")))
			#print("doi-xong")
		except:
			pass
	def xetcapcha(self):
		self.driver.switch_to.window (self.driver.window_handles [0])
		self.doi_captcha()
		captchagg()
		'''
		try:
			if(driver.find_element_by_id("captcha-golike").get_attribute("style") != "display: none;" and driver.find_element_by_id("captcha-golike").get_attribute("style") != ""):
				print("CÓ CAPTCHA")
				capcha()
				return True
		except:
			pass
			'''
		try:
			if(self.driver.find_element_by_id('swal2-content').get_attribute("style") != "display: block;"):
				return True
			cten = self.driver.find_element_by_id('swal2-content')
			
			try:
				WebDriverWait(self.driver, 0.1).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]")))
				try:
					self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				except:
					pass
				return True
			except:
				pass
			if(cten.text.find('Hệ thống jobs đang trong quá trình xử lý chặn auto và phân phối jobs') != -1):
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok

				return True
			elif(cten.text.find('Không tải được danh sách Job do tài khoản Facebook bị khóa. Nếu tài khoản không bị khóa hãy vào menu tài khoản và Cập nhật lại thông tin tài khoản.') != -1 ):
				self.driver.get("https://golike.mobi/account/manager/facebook")
				self.sleep13()
				self.driver.execute_script("document.getElementsByClassName('material-icons float-right d200 hand')[0].click()")
				time.sleep(1)
				self.driver.execute_script("document.getElementsByClassName('d-block')[9].click()")
				self.sleep13()
				self.lay_jobs()
				return True
			if(cten.text.find('Đã gửi thông tin lên hệ thống xét duyệt') != -1 ):
				print(cten.text[(len(cten.text)-3):len(cten.text)])
				self.tongsojob +=1
				self.sojobhuy = 0
				self.bi_google_chan = 0
				self.recaptcha_button = 0
				self.nuoi_fb()
				if(self.tongsojob > self.sojob ):
					print("=============================đủ ",self.sojob,"============================")
					self.countfage=0
					self.tongsojob=0
					self.driver.quit()
					self.tang += 1
					minimain(self.index)
			if ( cten.text.find('Không thể báo cáo hoàn thành lại do đã hết') != -1 ):
				print(cten.text)
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				
				self.doi_load()
				return False
			if(cten.text.find('Để đảm bảo công bằng cho mọi người') != -1 and sonick > 2):
				print("đổi IP mạng > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > ")
				self.doiIPmang()
				self.driver.quit()
				print("chỉ được dùng 2 fb trên 1 ip mạng ------------------------------------------------------------------------------")
				input()
			if(cten.text.find('Hệ thống đang tự động phân phối tối ưu jobs') != -1 or cten.text.find('timeout of 0ms exceeded') != -1 ):
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				time.sleep(60)
				
				return True
			if(  cten.text.find('Tài khoản của bạn KHÔNG sẵn sàng làm jobs like page') != -1  or cten.text.find('Đã gửi báo cáo lên hệ thống') != -1   ):
				
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				return True

			if(cten.text.find('Bạn chưa làm việc, không thể bấm hoàn thành') != -1 or cten.text.find('Bài viết đã đủ số lượng') != -1  or cten.text.find('Bài viết này đã bị ẩn khi bị mọi người báo cáo lỗi quá nhiều') != -1 or cten.text.find('Không thể báo cáo hoàn thành do bạn đã làm công việc này rồi') != -1 ):
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				self.to_cao(3)
				return True
			if(cten.text.find('Vui lòng cập nhật phiên bản mới nhất để làm việc') != -1 or cten.text.find('thử lại sau ít phút') != -1 or cten.text.find('Thao tác quá nhanh vui lòng làm chậm lại 1 xíu nhé bạn !') != -1  or cten.text.find('Error') != -1 or cten.text.find('quá nhanh') != -1):
				self.lamtiep()
				return True
			if(cten.text.find('chưa thực hiện thao tác') != -1 or cten.text.find(' hết hạn hoàn thành') != -1 ):
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				self.to_cao(2)
				return True
			if(cten.text.find('quá 100 jobs') != -1 or cten.text.find('ghỉ ngơi để đảm bảo sức khỏe và quay lại vào ngày mai để làm việc tiếp nhé') != -1 or cten.text.find('Bạn đã nhập sai câu hỏi xác nhận quá 3 lần') != -1):
				print("=============================Bạn đã làm quá 100 jobs ============================")
				self.countfage=0
				self.tongsojob=0
				self.driver.quit()
				self.tang += 1
				self.minimain(self.index)
			if(cten.text.find('hoàn thành lại thành công') != -1 ):
				self.driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				return True
			else:
				print(cten.text)
				self.lay_jobs()
				#playsound("C:\withpython\gun0.mp3",block=False)
				
		except:
			return True

	

def minimain ():

	while (True):
		
		#random.randint(99,100)
		

		driver1 = DRIVER()
		#driver2 = DRIVER()
		
		
		driver1.driver.get("https://golike.mobi/home")
		#driver2.driver.get("https://golike.mobi/home")
		input()

sonick  = 1

sojobhuy = 0 
if __name__ == '__main__':
	minimain()