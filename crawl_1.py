from selenium import webdriver
import time 
import requests
from PIL import Image

def initDriver(filepath):
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\'+ filepath) 
	'''
	mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/535.19" }
	options.add_experimental_option("mobileEmulation", mobile_emulation)
	'''
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', options=options)
	return driver

def getimg(a,s,td):
	response = requests.get(a)
	file = open("C:\\Users\\tiepl\\Desktop\\anh_captcha_google\\w"+str(s)+".png", "wb")
	file.write(response.content)
	file.close()
	img =  Image.open("C:\\Users\\tiepl\\Desktop\\anh_captcha_google\\w"+str(s)+".png")
	row,col = img.size
	img.close()
	
	demsize((str(row) + ' x ' + str(col)) , td)

def demsize(sz,td):
	global sizee,buttonn
	if(len(sizee) < 1):
		sizee.append(sz)
		buttonn.append(td)
		print(sz,td)
		
	else:
		for i in range(0,len(sizee)):
			if(sizee[i] == sz and buttonn[i] == td):
				return True
		sizee.append(sz)
		buttonn.append(td)
		print(sz,td)
def doi_load():
	try:
		while(driver.find_elements_by_tag_name("img")[6].get_attribute("style") == 'display: none;'):
			pass
	except:
		return True

lst = []
sizee = []
buttonn = []

def timten(ten):
	global lst
	if(len(lst) < 1):
		lst.append(ten)
	else:
		for i in lst:
			if(i == ten):
				return True
		lst.append(ten)


if __name__ == '__main__':
	dem=0
	driver = initDriver('letiep8')

	while(1):
		driver.get('https://golike.mobi/jobs/facebook?load_job=true')
		
		driver.execute_script("javascript:for(run of document.getElementsByTagName('h6')){if(run.innerHTML=='mBasic' || run.innerHTML== 'Facebook' || run.innerHTML == 'Trình duyệt'){run.click();break;} }")#click giả vờ làm
		driver.switch_to.window (driver.window_handles [1])
		driver.close()
		driver.switch_to.window (driver.window_handles [0])
		doi_load()
		time.sleep(2)
		driver.execute_script("javascript:for(run of document.getElementsByTagName('h6')){if(run.innerHTML=='Bấm hoàn thành để nhận tiền sau khi làm việc xong.'){run.click()} }")
		doi_load()
		
		try:
			while(1):
				driver.switch_to.window (driver.window_handles [0])
				driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[2])
				
				ten = driver.find_element_by_tag_name('strong').text
				timten(ten)

				td = driver.find_elements_by_tag_name('td')
				for i in driver.find_elements_by_tag_name('img'):
					getimg(i.get_attribute('src'),dem,len(td))
					dem+=1
					if(len(driver.find_elements_by_tag_name('img')) > 1):
						if(driver.find_elements_by_tag_name('img')[0].get_attribute('src') == driver.find_elements_by_tag_name('img')[1].get_attribute('src')):
							break
				#if(dem % 200 == 0):
				#	break
				driver.find_element_by_id('recaptcha-reload-button').click()#nut load lai captcha
				time.sleep(0.2)
		except:
			f = open('C:\\Users\\tiepl\\Desktop\\tencauhoi.txt','a')
			for xd in lst:
				f.write("\n")
				f.write(str(xd))
			f.write("\n")
			f.close()
			f = open('C:\\Users\\tiepl\\Desktop\\size_and_button.txt','a')
			for i in range(0,len(sizee)):
				f.write("\n")
				f.write(str(sizee[i]))
				f.write(" _ ")
				f.write(str(buttonn[i]))
			f.write("\n")
			f.close()


	