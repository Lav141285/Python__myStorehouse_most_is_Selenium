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
sojob = 40
def initDriver(filepath):
    
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\'+ filepath) 
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	browser = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', chrome_options=options)
	return browser

'''
	mobile_emulation = {
	"deviceMetrics": { "width": 1600, "height": 900, "pixelRatio": 3.0 },
	"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
	}

	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\'+ filepath) 

	options.add_experimental_option("mobileEmulation", mobile_emulation)

	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	
	browser = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', chrome_options=options)
	return browser
	'''


def suly(img):
	global somauchu
	somauchu = 0
	row,col = img.size
	pixels=img.load()
	xtam=int(row/2)
	#tim start
	chaystart = 0
	#chạy đến captcha 
	while (True):
		start = xtam-10
		end = xtam+10
		dk= True
		while(start < end):
			#nếu là màu nền
			dk1=bool(218 == pixels[start,chaystart][0] and 112 == pixels[start,chaystart][1] and 214 == pixels[start,chaystart][2] )
			dk2=bool(165 == pixels[start,chaystart][0] and 42 == pixels[start,chaystart][1] and 42 == pixels[start,chaystart][2] )
			dk3=bool(128 == pixels[start,chaystart][0] and 128 == pixels[start,chaystart][1] and 128 == pixels[start,chaystart][2] )
			dk4=bool(128 == pixels[start,chaystart][0] and 0 == pixels[start,chaystart][1] and 128 == pixels[start,chaystart][2] )
			dk5=bool(0 == pixels[start,chaystart][0] and 0 == pixels[start,chaystart][1] and 0 == pixels[start,chaystart][2] )
			dk *= bool( dk1 + dk2 + dk3 + dk4 + dk5 )
			start +=1
			if(dk == False):
				#pixels[start,chaystart]=(0,0,0)
				break
			
		if(dk == True):
			break
		chaystart+=1
	#tim end
	chayend = chaystart+50
	#chạy đến captcha từ treen xuống cuối captcha
	while (True):
		start = xtam-10
		end = xtam+10
		dk= True
		while(start < end):
			#nếu là màu nền
			dk1=bool(255 == pixels[start,chayend][0] and 255 == pixels[start,chayend][1] and 255 == pixels[start,chayend][2] )
			dk *= dk1
			start +=1
			#pixels[start,chayend]=(0,0,0)
			if(dk == False):
				break
			
		if(dk == True):
			break
		chayend+=1
		if(chayend == col):
			break
	chayend-=2
	ytam=((chayend-chaystart)/2+chaystart)
	# tim x max
	chay=0
	so_lan_true = 0
	while (so_lan_true <= 55 ):
		#cho duyệt 1 cột pixel từ tâm ra ngoài , nếu cột này có các màu bằng nhau thì lấy làm mốc xmax
		start = chaystart+1
		end = chayend-1
		dk= True
		while(start < end):
			dk *= bool( pixels[xtam+chay,ytam][0] ==  pixels[xtam+chay,start][0] and pixels[xtam+chay,ytam][1] ==  pixels[xtam+chay,start][1] and pixels[xtam+chay,ytam][2] ==  pixels[xtam+chay,start][2])
			start +=1
			if(dk == False):
				so_lan_true = 0
				break
			
		if(dk == True):
			so_lan_true +=1
		chay+=1
	xmax = xtam+chay-55

	#tim x min
	chay=0
	so_lan_true = 0
	while (so_lan_true <= 55):
		start = chaystart
		end = chayend
		dk= True
		while(start < end):
			dk *= bool( pixels[xtam+chay,ytam][0] ==  pixels[xtam+chay,start][0] and pixels[xtam+chay,ytam][1] ==  pixels[xtam+chay,start][1] and pixels[xtam+chay,ytam][2] ==  pixels[xtam+chay,start][2])
			start +=1
			if(dk == False):
				so_lan_true = 0
				break
			
		if(dk == True):
			so_lan_true +=1
		chay-=1
	xmin = xtam+chay+55
	##############################################################################################################################################

	#sử lí ảnh 
	img = img.crop((xmin,chaystart, xmax,chayend))
	img_data = img.getdata()

	lst=[]
	for i in img_data:
		#nếu là màu chữ
		dk1=bool(0 == i[0] and 0 == i[1] and 255 == i[2] )
		dk2=bool(255 == i[0] and 165 == i[1] and 0 == i[2] )
		dk3=bool(0 == i[0] and 128 == i[1] and 0 == i[2] )
		dk4=bool(0 == i[0] and 255 == i[1] and 255 == i[2] )
		dk5=bool(255 == i[0] and 215 == i[1] and 0 == i[2] )
		dk6=bool(255 == i[0] and 255 == i[1] and 255 == i[2] )
		dk7=bool(255 == i[0] and 0 == i[1] and 0 == i[2] )
		
		dk = bool( dk1 + dk2 + dk3 + dk4 + dk5 + dk6 + dk7 )
		if (dk):
			lst.append(0)
			somauchu+=1
		else:
			lst.append(255)
		
	new_img = Image.new("L", img.size)
	new_img.putdata(lst)

	return image_to_string(new_img,lang="vie")

def doi():
	try:
		x=driver.find_element_by_class_name("toast-message")
		#print(x.text)
		time.sleep(0.01)
		doi()
	except:
		return True
def capcha(xy):
	#--------------------------------------------------------------------------------------
	global tang,somauchu
	somauchu=0
	driver.switch_to.window (golike)
	#print("Bắt đầu giải captcha")
	driver.set_window_size(1900, 1400)
	time.sleep(0)
	#document.getElementsByClassName("b200 font-bold mb-0 font-15 text-capitalize block-text")[12].scrollIntoView(true)
	driver.execute_script("document.getElementsByClassName('group-icon')[0].scrollIntoView(true);")
	time.sleep(0.1)
	doi()
	driver.get_screenshot_as_file("d:\capcha"+taikhoanx+".png")
	image =  Image.open("d:\capcha"+taikhoanx+".png")
	key_captcha = suly(image)
	#print(key_captcha)
	if os.path.exists("d:\capcha"+taikhoanx+".png"):
			os.remove("d:\capcha"+taikhoanx+".png")

	#su ly key_captcha
	kt=key_captcha[len(key_captcha)-1]
	#print('___________',kt)
	key_captcha = re.sub( kt, '', key_captcha)
	key_captcha = re.sub('\?|\'|\§|\ |\:|\\n','', key_captcha)
	print(key_captcha,"->",somauchu)
	#lay dap an
	dapan=0
	j=0
	if(key_captcha.find('NAM') > -1  ):
		dapan=7
	if(key_captcha.lower().find('2b') > -1  ):
		dapan=10
	if(key_captcha.find('ONH') > -1  ):
		dapan=5
	if(key_captcha.lower().find('tám') > -1  ):
		dapan=8
	if(key_captcha.find('GO') > -1  ):
		dapan=6
	if(key_captcha.lower().find('gườicóbaonhiêuchân') > -1  ):
		dapan=2
	if(key_captcha.find('9+') > -1  ):
		dapan=10
	if(key_captcha.lower().find('chinl') > -1  ):
		dapan=9
	if(key_captcha.lower().find('trăng') > -1  ):
		dapan=1
	if(key_captcha.lower().find('taycái') > -1  ):
		dapan=2
	if(key_captcha.lower().find('mộil') > -1  ):
		dapan=1
	if(key_captcha.lower().find('năm') > -1  ):
		dapan=5
	if(key_captcha.lower().find('chữnh') > -1  ):
		dapan=4
	if(key_captcha.lower().find('emáy') > -1  ):
		dapan=2
	if(key_captcha.lower().find('mộtl') > -1  ):
		dapan=1
	if(key_captcha.lower().find('lợn') > -1  ):
		dapan=4
	if(key_captcha.find('1+6') > -1  ):
		dapan=7
	if(key_captcha.lower().find('†b') > -1  ):
		dapan=5
	if(key_captcha.lower().find('mười') > -1  ):
		dapan=10
	if(key_captcha.lower().find('tamgiác') > -1  ):
		dapan=3
	if(key_captcha.lower().find('gà') > -1  ):
		dapan=2
	if(key_captcha.lower().find('vị') > -1  ):
		dapan=2
	if(key_captcha.lower().find('onv') > -1  ):
		dapan=2
	if(key_captcha.find('isao') > -1  ):
		dapan=5
	if(key_captcha.find('Nam') > -1  ):
		dapan=1
	if(key_captcha.find('KE') > -1  ):
		dapan=6
	if(key_captcha.lower().find('bảy') > -1  ):
		dapan=7
	if(key_captcha.find('EB') > -1  ):
		dapan=8
	if(key_captcha.find('IP') > -1  ):
		dapan=8
	if(key_captcha.lower().find('nhiêugiờ') > -1  ):
		dapan=1
	if(key_captcha.find('I+rO=') > -1  ):
		dapan=7
	if(key_captcha.find('K2{7(VIÍCCĐÝ/') > -1  ):
		dapan=4
	if(key_captcha.lower().find('1tuần') > -1  ):
		dapan=7
	if(key_captcha.lower().find('cáivòi') > -1  ):
		dapan=1
	if(key_captcha.lower().find('ô') > -1  and key_captcha.lower().find('bánh') > -1 ):
		dapan=4
	if(key_captcha.lower().find('ổ') > -1  and key_captcha.lower().find('bánh') > -1 ):
		dapan=4
	if(key_captcha.lower().find('â') > -1  and key_captcha.lower().find('bánh') > -1 ):
		dapan=2
	if(key_captcha.find('tuần') > -1  ):
		dapan=7
	if(key_captcha.lower().find('ạ') > -1  and key_captcha.lower().find('bánh') > -1 ):
		dapan=2
	if(key_captcha.lower().find('á') > -1  and key_captcha.lower().find('bánh') > -1 ):
		dapan=2
	if(key_captcha.lower().find('ôtõ') > -1  ):
		dapan=4
	if(key_captcha.lower().find('eôt') > -1  ):
		dapan=4
	if(key_captcha.find('Ở+I') > -1  ):
		dapan=10
	if(key_captcha.lower().find('bốn') > -1  ):
		dapan=4
	if(key_captcha.find('2/7{llIll1ÍCCD') > -1  ):
		dapan=9
	if(key_captcha.find('SØĐaiaS') > -1  ):
		dapan=3
	if(key_captcha.find('IL(2lIiIiUchân') > -1  ):
		dapan=2
	if(key_captcha.find('di)CỔd4nhiêubánh') > -1  ):
		dapan=2
	if(key_captcha.find('-5=') > -1  ):
		dapan=3
	if(key_captcha.lower().find('sáu') > -1  ):
		dapan=6
	if(key_captcha.find('NAM') > -1  ):
		dapan=7
	if(key_captcha.lower().find('eđạp') > -1  ):
		dapan=2
	if(key_captcha.lower().find('châncái') > -1  ):
		dapan=2
	if(key_captcha.lower().find('hvuông') > -1  ):
		dapan=4
	if(key_captcha.lower().find('hail') > -1  ):
		dapan=2
	if(key_captcha.find('VIEW') > -1  ):
		dapan=6
	if(key_captcha.lower().find('chín') > -1  ):
		dapan=9
	if(key_captcha.lower().find('nvoi') > -1  ):
		dapan=1
	if(key_captcha.lower().find('điệnthoại') > -1  ):
		dapan=10
	if(key_captcha.lower().find('cò') > -1  ):
		dapan=2
	if(key_captcha.lower().find('1tiếng') > -1  ):
		dapan=1
	if(key_captcha.find('LUB') > -1  ):
		dapan=6
	if(key_captcha.find('GL') > -1  ):
		dapan=6
	if(key_captcha.lower().find('mắt') > -1  ):
		dapan=2
	if(key_captcha.lower().find('nchó') > -1  ):
		dapan=4
	if(key_captcha.lower().find('balàs') > -1  ):
		dapan=3
	if(key_captcha.lower().find('1b') > -1  ):
		dapan=5
	if(key_captcha.lower().find('ườicóbaonhiềuch') > -1  ):
		dapan=2
	if(key_captcha.lower().find('trời') > -1  ):
		dapan=1
	if(key_captcha.find('2+') > -1  ):
		dapan=5
	if(key_captcha.lower().find('gườicóbaonhiễuchân') > -1  ):
		dapan=2

	if(dapan == 0):
		print("chọn bừa")
		dapan=3

	#time.sleep(53)
	print('-------DAP AN CUA CAPTCHA LA---------: ', dapan)
	
	#DA CO DAP AN , BAT DAU RECAPTCHA
	if (dapan == 1 ):
		driver.find_element_by_tag_name('select').send_keys(str(dapan))
		time.sleep(0.1)
	driver.find_element_by_tag_name('select').send_keys(str(dapan))
	time.sleep(0.1)
	dapan=0
	somauchu=0
	if(xy == 1 ):
		driver.execute_script("document.getElementsByTagName('button')[1].click()")
	if (xy == 2 ):
		driver.execute_script("document.getElementsByTagName('button')[3].click()")
	time.sleep(0)
	if(xy ==1 ):
		doibangthongbaotat()
		doicaptcha()
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
	#else:
	#	xetcapchainstar()
def doicaptcha():
	dem=0
	while(dem<20):
		try:
			if(driver.find_element_by_id("captcha-golike").get_attribute("style") == "display: block;"):
				time.sleep(0.1)
				dem+=1
			else:
				return True
		except:
			return True
def doicaptchabat():
	dem=0
	while(dem<20):
		try:
			if(driver.find_element_by_id("captcha-golike").get_attribute("style") == "display: block;"):
				return True
			else:
				time.sleep(0.1)
				dem+=1	
		except:
			return True

def doibangthongbaotat():
	dem=0
	while(dem<20):
		try:
			x = driver.find_element_by_id('swal2-content')
			try:
				x.click()
			except:
				time.sleep(0.1)
			time.sleep(0.1)
			dem+=1
		except:
			return True
def xetcapcha():
	
	global tang,golike,tongsojob,countfage,sojobhuy,lai
	#print(" ------------ĐANG XÉT CAPTCHA ------------------")
	driver.switch_to.window (driver.window_handles [0])
	time.sleep(0)
	try:
		if(driver.find_element_by_id("captcha-golike").get_attribute("style") == "display: block;"):
			print("CÓ CAPTCHA")
			capcha(1)

		#print("có captcha")

		
		#print("có captcha")
	except:
		time.sleep(0.1)# không có captcha
	try:
		cten = driver.find_element_by_id('swal2-content')
		#print(cten.text)
		
		if(cten.text.find('Hệ thống jobs đang trong quá trình xử lý chặn auto và phân phối jobs') != -1):
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			driver.execute_script("window.open('https://golike.mobi/jobs/facebook?load_job=true','_blank')")
			driver.switch_to.window (golike)
			driver.close()
			wind = driver.window_handles
			for i in wind:
				if( i!= golike):
					driver.switch_to.window (i)
					break
			golike=i
			
			doibangthongbaotat()
			doicaptcha()
			xetcapcha()
			doibangthongbaotat()
			doicaptcha()
			return True
		if(cten.text.find('Đã gửi thông tin lên hệ thống xét duyệt') != -1 ):
			print(cten.text[(len(cten.text)-2):len(cten.text)])
			tongsojob +=1
			sojobhuy = 0
			nuoi_fb()
			if(tongsojob > sojob or int(cten.text[(len(cten.text)-2):len(cten.text)]) > sojob):
				time.sleep(1)
				print("=============================CHUYỂN NICK NÀO ============================")
				countfage=0
				tongsojob=0
				driver.quit()
				tang += 1
				minimain(index)
		if ( cten.text.find('Không thể báo cáo hoàn thành lại do đã hết') != -1 ):
			print(cten.text)
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			doibangthongbaotat()
			doicaptcha()
			doibangthongbaotat()
			doicaptcha()
			return False
		if(cten.text.find('Hệ thống đang tự động phân phối tối ưu jobs') != -1 or cten.text.find('timeout of 0ms exceeded') != -1 or  cten.text.find('Để đảm bảo công bằng cho mọi người') != -1 or cten.text.find('Tài khoản của bạn KHÔNG sẵn sàng làm jobs like page') != -1  or cten.text.find('Đã gửi thông tin lên hệ thống xét duyệt') != -1 or cten.text.find('Đã gửi báo cáo lên hệ thống') != -1  or cten.text.find('hoàn thành lại thành công') != -1  ):
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			doibangthongbaotat()
			doicaptcha()
			xetcapcha()
			doibangthongbaotat()
			doicaptcha()
			return True
		if(cten.text.find('Bạn chưa làm việc, không thể bấm hoàn thành') != -1 or cten.text.find('Bài viết đã đủ số lượng') != -1  or cten.text.find('Bài viết đã hết hạn hoàn thành') != -1 or cten.text.find('Bài viết này đã bị ẩn khi bị mọi người báo cáo lỗi quá nhiều') != -1 or cten.text.find('Không thể báo cáo hoàn thành do bạn đã làm công việc này rồi') != -1 ):
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			doibangthongbaotat()
			doicaptcha()
			to_cao()
			doibangthongbaotat()
			doicaptcha()
			return True 
		if(cten.text.find('chưa thực hiện thao tác') != -1 or cten.text.find('Thao tác quá nhanh vui lòng làm chậm lại 1 xíu nhé bạn !') != -1 or cten.text.find('Error') != -1 or cten.text.find('quá nhanh') != -1 or cten.text.find('Vui lòng cập nhật phiên bản mới nhất để làm việc') != -1 or cten.text.find('Vui lòng thử lại sau ít phút, hoặc liên hệ admin để hỗ trợ') != -1):
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			lai = 0
			try:
				try:
					doibangthongbaotat()
					doicaptcha()
					if (lai > 2 ):
						to_cao()
						doibangthongbaotat()
						doicaptcha()
						return True 
					tim=0
					mbasic1= driver.find_elements_by_tag_name("h6")
					dem=0
					for mb1 in mbasic1:
						if(mb1.text == "Hoàn thành"):
							lai += 1
							xetcapcha()
							doibangthongbaotat()
							doicaptcha()
							driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
							tim=1
							break
						dem+=1
					if(tim == 0):
						to_cao()
						return True
				except:							
					to_cao()
					return True
				driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
				doibangthongbaotat()
			except:
				to_cao()
			return True
		if(cten.text.find('quá 100 jobs') != -1 or cten.text.find('ghỉ ngơi để đảm bảo sức khỏe và quay lại vào ngày mai để làm việc tiếp nhé') != -1 or cten.text.find('Bạn đã nhập sai câu hỏi xác nhận quá 3 lần') != -1):
			print("Bạn đã làm quá 100 jobs")
			driver.execute_script("document.getElementsByClassName('swal2-confirm swal2-styled')[0].click()")#nhan ok
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
		else:
			print(cten.text,"\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			#playsound("gun0.mp3",block=False)
			
	except:
		return True
	'''
	
		else:
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			#input()
			print("=============================LÀM LẠI THÔI============================")
			driver.quit()
			minimain(index)
	#time.sleep(3)
	'''

def to_cao():
	global countfage,tongsojob,tang,sojobhuy
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	print("đang tố cáo")
	sojobhuy += 1
	try:
	#nhấn báo lỗi
		tocao= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in tocao:
			if(mb1.text.lower() == "báo lỗi"):
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
			dem+=1
	#Tôi không muốn làm Job này
		dem=0
		for mb1 in tocao:
			if(mb1.text == "Tôi không muốn làm Job này"):
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
			dem+=1
	#nhấn gửi 
		driver.execute_script("document.getElementsByClassName('btn btn-primary btn-sm form-control mt-3')[0].click()")
	except:
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
	doibangthongbaotat()
	doicaptcha()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
def like_fage():
	global countfage,tongsojob,tang
	driver.switch_to.window (driver.window_handles [0])
	
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptchabat()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai = 1 
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:	
		print("không nhấn mbasic")						
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	driver.switch_to.window (driver.window_handles [1])
	
	try:
		if(loai == 1 ):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,5))
			driver.execute_script("window.scrollTo(0, 0);")
			driver.execute_script("document.getElementsByClassName('ct')[0].click()")#nhanlikefage
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(random.randint(1,5))
			driver.execute_script("window.scrollTo(0, 0);")
			time.sleep(random.randint(1,2))
			driver.execute_script("document.getElementsByClassName('ct')[0].click()")#nhanlikefage
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		driver.close()
		driver.switch_to.window (golike)
		time.sleep(0.2)
	
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
#nhấn hoàn thành 
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
				
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoàn thành")
			to_cao()
			return True
		
	except:
		huy_job()
	time.sleep(0.1)
	doibangthongbaotat()
	doicaptchabat()
	xetcapcha()
	
	
	countfage+=1
	return True	
def theo_doi():
	global countfage,tongsojob,tang
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptchabat()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai=1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhấn mbasic")					
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	
#nhấn theo dõi
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Theo dõi").click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Theo dõi").click()
			time.sleep(random.randint(1,2))
	except:
		time.sleep(0.2)
	
	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	driver.close()
	driver.switch_to.window (golike)
	
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	dem=0
	for mb1 in mbasic1:
		if(mb1.text == "Hoàn thành"):
			
			xetcapcha()
			
			driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
			tim=1
			break
		dem+=1
	if(tim == 0):
		print("không có hoan thanh")
		to_cao()
		return True
	doibangthongbaotat()
	doicaptchabat()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	
	return True	
def like_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhấn mbasic")						
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[0].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,2))
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[0].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
	
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
			
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoàn thành")
			to_cao()
			return True
		time.sleep(0.5)
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
		
		
	except:
		huy_job()
	
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def thuong_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhấn mbasic")					
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[2].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[2].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
				
				xetcapcha()
			
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()

		
	except:
		huy_job()
	time.sleep(0.1)

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def love_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhan mbasic")
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[1].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,2))
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[1].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
				
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
		
		
	except:
		huy_job()
	time.sleep(0.1)

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def phanno_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhấn mbasic")						
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[6].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[6].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
			
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()	
		xetcapcha()
		
		
	except:
		huy_job()
	time.sleep(0.1)

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def buon_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:	
		print("không nhan mbasic")					
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[5].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[5].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
				
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
		
		
	except:
		huy_job()
	time.sleep(0.1)

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def tang_comment():
	global countfage,tongsojob,tang
	driver.switch_to.window (driver.window_handles [0])
	try:
		driver.execute_script("document.getElementsByTagName('u')[0].click()")#nhan copy
		driver.execute_script("document.getElementsByTagName('u')[0].click()")#nhan copy
	except:
		time.sleep(0.1)
	
	comment = driver.find_elements_by_tag_name("span")[7].text
	mbasic= driver.find_elements_by_tag_name("h6")
	dem=0
	for mb in mbasic:
		if(mb.text.lower().find("mb") > -1):
			driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
		dem+=1
	driver.switch_to.window (driver.window_handles [1])
	time.sleep(random.randint(1,5))
	driver.find_element_by_name("comment_text").send_keys(comment)
	time.sleep(random.randint(3,4))
	inp = driver.find_elements_by_tag_name("input")
	dem=0
	for ip in inp :
		if (ip.get_attribute("value") == "Bình luận"):
			driver.execute_script("document.getElementsByTagName('input')["+str(dem)+"].click()")
		dem+=1
	time.sleep(random.randint(1,2))
	driver.close()
	driver.switch_to.window (driver.window_handles [0])
	time.sleep(0.1)
	dem=0
	for mb in mbasic:
		if(mb.text == "hoàn thành"):
			driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
		dem+=1
	doibangthongbaotat()
	doicaptchabat()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def lamviec ():
	global golike,countfage,sojobhuy,tongsojob,tang
	if (sojobhuy > 30 ):
		print("=============================toang r============================")
		sojobhuy =0
		countfage=0
		tongsojob=0
		driver.quit()
		tang += 1
		minimain(index)
	time.sleep(0.1)
	try:
		baotri = driver.find_elements_by_tag_name("h5")
		for bao in baotri :
			if (bao.text.find("HỆ THỐNG ĐANG PHÂN PHỐI JOBS") != -1):
				print("HỆ THỐNG ĐANG PHÂN PHỐI JOBS")
				time.sleep(120)
			elif(bao.text.find("Chưa Có Tài Khoản") != -1):
				driver.execute_script("document.getElementsByClassName('font-20 d-block mb-1 icon-home')[0].click()")
				time.sleep(2)
				driver.execute_script("document.getElementsByClassName('font-20 d-block mb-1 icon-wallet')[0].click()")
				time.sleep(0)
				driver.get("https://golike.mobi/jobs/facebook?load_job=true")
				time.sleep(0)
	except:
		pass 
	
	
	doibangthongbaotat()
	doicaptcha()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	win1 = driver.window_handles
	for j in win1:
		if(j != golike):
			driver.switch_to.window (j)
			driver.close()
	driver.switch_to.window (golike)
	
	try:
		try:
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]")))
		except:
			doibangthongbaotat()
			doicaptcha()
			xetcapcha()
			doibangthongbaotat()
			doicaptcha()
		WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/span/div[1]")))
		driver.execute_script("document.getElementsByClassName('card mb-2 hand')[0].click()")#nhan job
		xacnhan = driver.find_elements_by_tag_name('span')
		print(xacnhan[5].text,datetime.now().hour,"giờ",datetime.now().minute, "phút",datetime.now().second,"giây")
		if (xacnhan[5].text == 'TĂNG LIKE CHO FANPAGE'):
			
			if(countfage < random.randint(10,13)):
				like_fage()
			else:
				to_cao()
		elif(xacnhan[5].text == 'TĂNG LIKE CHO BÀI VIẾT'):
			like_bai()
		elif(xacnhan[5].text == 'TĂNG THƯƠNG THƯƠNG CHO BÀI VIẾT'):
			thuong_bai()
		elif(xacnhan[5].text == 'TĂNG LOVE CHO BÀI VIẾT'):
			love_bai()
		elif(xacnhan[5].text == 'TĂNG HAHA CHO BÀI VIẾT'):
			haha_bai()
		elif(xacnhan[5].text == 'TĂNG WOW CHO BÀI VIẾT'):
			wow_bai()
		elif(xacnhan[5].text == 'TĂNG SAD CHO BÀI VIẾT'):
			buon_bai()
		elif(xacnhan[5].text == 'TĂNG ANGRY CHO BÀI VIẾT'):
			phanno_bai()
		elif(xacnhan[5].text == 'TĂNG COMMENT CHO BÀI VIẾT'):
			tang_comment()
		elif(xacnhan[5].text == 'TĂNG LƯỢT THEO DÕI'):
			theo_doi()
		else:
			print("ngoại lệ : không biết đây là job gì ")
			
			doibangthongbaotat()
			doicaptcha()
			xetcapcha()
			doibangthongbaotat()
			doicaptcha()
	except:
		driver.execute_script("window.open('https://golike.mobi/jobs/facebook?load_job=true','_blank')")
		driver.switch_to.window (golike)
		driver.close()
		wind = driver.window_handles
		for i in wind:
			if( i!= golike):
				driver.switch_to.window (i)
				golike=i
				break
	return True
def huy_job():
	try:
		driver.switch_to.window (driver.window_handles [1])
	except:
		return True
	driver.close()
	driver.switch_to.window (driver.window_handles [0])
	doibangthongbaotat()
	doicaptcha()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	to_cao()
	doibangthongbaotat()
	doicaptcha()
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
def haha_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhan mbasic")						
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[3].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[3].click()
			time.sleep(random.randint(1,2))
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
			
				xetcapcha()
		
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
	
		
	except:
		huy_job()
	time.sleep(0.1)
	
	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def wow_bai():
	global tang,tongsojob,countfage
	driver.switch_to.window (driver.window_handles [0])
	tim=0
	try:
		mbasic1= driver.find_elements_by_tag_name("h6")
		dem=0
		for mb1 in mbasic1:
			
			if(mb1.text.lower().find("mb") > -1):
				doibangthongbaotat()
				doicaptcha()
				xetcapcha()
				doibangthongbaotat()
				doicaptcha()
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				loai =1
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có mbasic")
			driver.execute_script("document.getElementsByTagName('h6')[2].click()")
			loai=2
	except:
		print("không nhan mbasic")			
		to_cao()
		return True

	time.sleep(random.randint(1,2))
	driver.switch_to.window (driver.window_handles [1])
	#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
	inputdangnhap = driver.find_elements_by_tag_name("input")
	
	for ip in inputdangnhap :
		if (ip.get_attribute("value").lower() == "đăng nhập"):
			f = open('tk_bi_dang_xuat.txt','a')
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
			f.write(taikhoanx)
			f.close()
			print("=============================CHUYỂN NICK NÀO ============================")
			countfage=0
			tongsojob=0
			driver.quit()
			tang += 1
			minimain(index)
	time.sleep(0.1)
	
	try:
		if(loai == 1):
			time.sleep(random.randint(1,5))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[4].click()
			time.sleep(random.randint(1,2))
		if(loai == 2):
			d = driver.current_url
			vt = d.find('facebook')
			driver.get('https://mbasic.'+d[vt:len(d)])
			time.sleep(random.randint(1,5))
			time.sleep(random.randint(1,2))
			driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
			time.sleep(random.randint(1,2))
			nhan=driver.find_elements_by_tag_name('li')
			nhan[4].click()
			time.sleep(random.randint(1,2))
			
		time.sleep(random.randint(1,2))
		try:
			j=driver.find_elements_by_tag_name("div")
			for i in j :
				if(i.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
					print(i.text)
					f = open('tk_bi_chan.txt','a')
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
					f.write(taikhoanx)
					f.write("\n")
					 
					f.close()
					playsound("gun1.mp3",block=False)
					countfage=0
					tongsojob=0
					driver.quit()
					tang += 1
					minimain(index)
		except:
			pass
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (golike)
		
		time.sleep(3)
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		dem=0
		for mb1 in mbasic1:
			if(mb1.text == "Hoàn thành"):
			
				xetcapcha()
				
				driver.execute_script("document.getElementsByTagName('h6')["+str(dem)+"].click()")
				tim=1
				break
			dem+=1
		if(tim == 0):
			print("không có hoan thanh")
			to_cao()
			return True
		doibangthongbaotat()
		doicaptchabat()
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		
	except:
		huy_job()
	time.sleep(0.1)

	xetcapcha()
	doibangthongbaotat()
	doicaptcha()
	return True
def lamviec_lm_lai ():
	global golike,countfage,sojobhuy,tongsojob,tang
	try:
		nuoi_fb()
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div/div[1]/div[2]/div[4]/div/div/div[2]/div[2]/a")))
		try:
			job = driver.find_elements_by_tag_name("a")
			
			# nut hoan thanh
		except:
			print("không lấy dc các nút ")
		x=0
		xetcapcha()
		if (xetcapcha() == False):
			print("asfafsfdad")
			x+=1
		doibangthongbaotat()
		doicaptcha()

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
			xetcapcha()
			if (xetcapcha() == False):
				print("asfafsfdad")
				x+=1
			doibangthongbaotat()
			doicaptcha()
			vt = d.find('facebook')
			link = 'https://mbasic.'+d[vt:len(d)]
			print(link)
			
			try:
				indexx=0
				while(indexx < len(add)):
					if(add[indexx].get_attribute("class") == 'font-bold'):
						break
					indexx += 1
				if (add[indexx+1+8*x].text.lower()== 'like'):
					print("like")
					driver.execute_script("window.open('"+str(link)+"','_blank')")
					driver.switch_to.window (driver.window_handles [1])
					time.sleep(random.randint(1,2))
					#tìm nút đăng nhập nếu chẳng may bị đăng xuất 
					inputdangnhap = driver.find_elements_by_tag_name("input")
					
					for ip in inputdangnhap :
						if (ip.get_attribute("value").lower() == "đăng nhập"):
							f = open('tk_bi_dang_xuat.txt','a')
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
							f.write(taikhoanx)
							f.close()
							print("=============================CHUYỂN NICK NÀO ============================")
							countfage=0
							tongsojob=0
							driver.quit()
							tang += 1
							minimain_lm_lai(index)
					time.sleep(random.randint(1,5))
					driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
					print("đã nhấn bày tỏ cảm xúc")
					time.sleep(random.randint(1,2))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[0].click()
					print("đã nhấn like")
					time.sleep(random.randint(1,2))
					try:
						j=driver.find_elements_by_tag_name("div")
						for errorfb in j :
							if(errorfb.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
								print(errorfb.text)
								f = open('tk_bi_chan.txt','a')
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
								f.write(taikhoanx)
								f.write("\n")
								 
								f.close()
								playsound("gun1.mp3",block=False)
								countfage=0
								tongsojob=0
								driver.quit()
								tang += 1
								minimain_lm_lai(index)
					except:
						pass
					driver.close()
					driver.switch_to.window (golike)
					time.sleep(1)
					driver.execute_script("document.getElementsByTagName('button')[2].click()")
					
					xetcapcha()
					if (xetcapcha() == False):
						print("asfafsfdad")
						x+=1
					doibangthongbaotat()
					doicaptcha()
				elif (add[indexx+1+8*x].text.lower()== 'haha'):
					print("haha")
					driver.execute_script("window.open('"+str(link)+"','_blank')")
					driver.switch_to.window (driver.window_handles [1])
					time.sleep(random.randint(1,2))
					inputdangnhap = driver.find_elements_by_tag_name("input")
					
					for ip in inputdangnhap :
						if (ip.get_attribute("value").lower() == "đăng nhập"):
							f = open('tk_bi_dang_xuat.txt','a')
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
							f.write(taikhoanx)
							f.close()
							print("=============================CHUYỂN NICK NÀO ============================")
							countfage=0
							tongsojob=0
							driver.quit()
							tang += 1
							minimain_lm_lai(index)
					time.sleep(random.randint(1,5))
					driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
					print("đã nhấn bày tỏ cảm xúc")
					time.sleep(random.randint(1,2))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[3].click()
					print("đã nhấn like")
					time.sleep(random.randint(1,2))
					try:
						j=driver.find_elements_by_tag_name("div")
						for errorfb in j :
							if(errorfb.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
								print(errorfb.text)
								f = open('tk_bi_chan.txt','a')
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
								f.write(taikhoanx)
								f.write("\n")
								 
								f.close()
								playsound("gun1.mp3",block=False)
								countfage=0
								tongsojob=0
								driver.quit()
								tang += 1
								minimain_lm_lai(index)
					except:
						pass
					driver.close()
					driver.switch_to.window (golike)
					time.sleep(1)
					driver.execute_script("document.getElementsByTagName('button')[2].click()")
					
					xetcapcha()
					if (xetcapcha() == False):
						print("asfafsfdad")
						x+=1
					doibangthongbaotat()
					doicaptcha()
				elif (add[indexx+1+8*x].text.lower()== 'love'):
					print("love")
					driver.execute_script("window.open('"+str(link)+"','_blank')")
					driver.switch_to.window (driver.window_handles [1])
					time.sleep(random.randint(1,2))
					inputdangnhap = driver.find_elements_by_tag_name("input")
					
					for ip in inputdangnhap :
						if (ip.get_attribute("value").lower() == "đăng nhập"):
							f = open('tk_bi_dang_xuat.txt','a')
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
							f.write(taikhoanx)
							f.close()
							print("=============================CHUYỂN NICK NÀO ============================")
							countfage=0
							tongsojob=0
							driver.quit()
							tang += 1
							minimain_lm_lai(index)
					time.sleep(random.randint(1,5))
					driver.find_element_by_link_text("Bày tỏ cảm xúc").click()
					print("đã nhấn bày tỏ cảm xúc")
					time.sleep(random.randint(1,2))
					nhan=driver.find_elements_by_tag_name('li')
					nhan[1].click()
					print("đã nhấn like")
					time.sleep(random.randint(1,2))
					try:
						j=driver.find_elements_by_tag_name("div")
						for errorfb in j :
							if(errorfb.text.lower().find("do trên tài khoản của bạn có một số hành động bất thường") > -1 ):
								print(errorfb.text)
								f = open('tk_bi_chan.txt','a')
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
								f.write(taikhoanx)
								f.write("\n")
								 
								f.close()
								playsound("gun1.mp3",block=False)
								countfage=0
								tongsojob=0
								driver.quit()
								tang += 1
								minimain_lm_lai(index)
					except:
						pass
					driver.close()
					driver.switch_to.window (golike)
					time.sleep(1)
					driver.execute_script("document.getElementsByTagName('button')[2].click()")
					
					xetcapcha()
					if (xetcapcha() == False):
						print("asfafsfdad")
						x+=1
					doibangthongbaotat()
					doicaptcha()
				else:
					print("ngoại lệ : không biết đây là job gì ",add[indexx+1].text.lower())
			except:
				huy_job_lm_lai()
				x+=1
		if(x >=len(job)-23):
			driver.quit()
			tang += 1
			minimain_lm_lai(index)
	except:
		driver.quit()
		tang += 1
		minimain_lm_lai(index)
	return False
def huy_job_lm_lai():
	try:
		driver.switch_to.window (driver.window_handles [1])
	except:
		return True
	driver.close()
	driver.switch_to.window (driver.window_handles [0])
def lam_fb_lm_lai():
	
	time.sleep(0.1)
	while (True):
		
		print("lam viec")
		if(bool(lamviec_lm_lai())==False):
			break
		
	return False


def minimain_lm_lai (x):
	#taikhoan =  ('tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13')
	taikhoan =  ('tieple247','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
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

def nuoi_fb():
	nuoi= random.randint(1,3)
	while(nuoi < 3):
		hientai =driver.current_window_handle
		n = random.randint(1,8)
		w = random.randint(1,99)
		if (n==1):
			driver.execute_script("window.open('https://mbasic.facebook.com/','_blank')") #trang chủ
		elif (n==2):
			driver.execute_script("window.open('https://mbasic.facebook.com/menu/bookmarks/?ref_component=mbasic_home_header&ref_page=%2"+"Fwap%2"+"Fhome.php&refid="+ str(w)+"','_blank')") # trang cá nhân
		elif (n==3):
			driver.execute_script("window.open('https://mbasic.facebook.com/messages/?ref_component=mbasic_home_header&ref_page=%2"+"Fwap%2"+"Fprofile_timeline.php&refid="+ str(w)+"','_blank')") # tin nhắn
		elif (n==4):
			driver.execute_script("window.open('https://mbasic.facebook.com/notifications.php?ref_component=mbasic_home_header&ref_page=MNotificationsController&refid="+ str(w)+"','_blank')") #thông báo 
		elif (n==5):
			driver.execute_script("window.open('https://mbasic.facebook.com/buddylist.php?ref_component=mbasic_home_header&ref_page=MMessagingThreadlistController&refid="+ str(w)+"','_blank')") #chat
		elif (n==6):
			driver.execute_script("window.open('https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=MChatBuddyListController','_blank')") #bạn bè 
		elif (n==7):
			driver.execute_script("window.open('https://mbasic.facebook.com/pages/?ref_component=mbasic_home_header&ref_page=XPagesBrowserController','_blank')") #trang 
		elif (n==8):
			driver.execute_script("window.open('https://mbasic.facebook.com/groups/?category=membership&ref_component=mbasic_home_header&ref_page=XGroupBrowseController&refid="+ str(w)+"','_blank')") #nhóm
		
		
		driver.switch_to.window (driver.window_handles [1]) 
		time.sleep(0.5)
		driver.execute_script("javascript:setInterval(function(){window.scrollBy(0,(Math.floor((Math.random() * 1) + 0)+1)*window.innerHeight);}, Math.floor((Math.random() * 5000) + 1000));")
		time.sleep(random.randint(5,15))
		wind = driver.window_handles
		for i in wind:
			if(i != hientai and i!= golike):
				driver.switch_to.window (i)
				driver.close()
		driver.switch_to.window (hientai)
		nuoi+=1
def lam_fb():
	
	time.sleep(0.1)
	while (True):
		
		xetcapcha()
		doibangthongbaotat()
		doicaptcha()
		print("lam viec")
		if(bool(lamviec())==False):
			break
		
	return False


def minimain (x):
	#taikhoan =  ('tieple247','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
	taikhoan =  ('tieple24','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17')
	global driver,taikhoanx,tang,index,golike,countfage,tongsojob,sojob
	
	index=x
	
	while (True):
		sojob = random.randint(80,100)
		countfage=0
		tongsojob=0
		if((index+tang*sonick) > len(taikhoan)-1):
			tang=0
			minimain_lm_lai(1)
		
		taikhoanx = taikhoan[index+tang*sonick]
		print(taikhoanx)
		if os.path.exists("d:\capcha"+taikhoanx+".png"):
			os.remove("d:\capcha"+taikhoanx+".png")
		driver = initDriver(taikhoanx)
		driver.get('https://golike.mobi/jobs/facebook?load_job=true')
		golike =  driver.current_window_handle
		
		chuyen=bool(lam_fb())
		if(chuyen == False):
			driver.quit()
			tang+=1

sonick  = 2
#def aa ():
#	Pool(sonick).map(minimain, range(0,sonick))
sojobhuy = 0 
if __name__ == '__main__':
	#aa()
	minimain(0)
	#document.getElementsByClassName("row align-items-center")[3].setAttribute('href','')
#
#document.getElementsByClassName("row align-items-center")[3].setAttribute('target','')
#<div id="toast-container" class="toast-top-right"><div class="toast toast-error" aria-live="assertive" style="opacity: 0.79913;"><div class="toast-message">Đã gửi yêu cầu lấy job, vui lòng quay lại sau 10 giây</div></div><div class="toast toast-error" aria-live="assertive" style="opacity: 0.764042;"><div class="toast-message">Đã gửi yêu cầu lấy job, vui lòng quay lại sau 10 giây</div></div></div>