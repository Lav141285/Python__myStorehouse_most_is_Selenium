from selenium import webdriver
import re,time
from playsound import playsound
from datetime import datetime
def initDriver(filepath):
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=c:\withpython\\account_facebook\\'+ filepath) 
	'''
	mobile_emulation = {
    "deviceMetrics": { "width": 640, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/535.19" }
	options.add_experimental_option("mobileEmulation", mobile_emulation)
	'''
	options.headless = True
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(executable_path=r'c:\withpython\chromedriver.exe', options=options)
	return driver 
tang=0

thunhap=0.00
anchac = 0.00
dangduyet =0.00
mattien=0
if __name__ == '__main__':
	taikhoan =  ('tieple247','tieple01','tieple02','tieple03','tieple04','tieple05','tieple06','tieple07','tieple08','tieple09','tieple10','tieple11','tieple12','tieple13','tieple15','tieple16','tieple17','tieple19',"tieple20",'tieple21','letiep1','letiep2','letiep3','letiep4','letiep5','letiep6','letiep7','letiep8')
	#taikhoan = ("tieple20",'tieple21','letiep1','letiep2','letiep3','letiep4','letiep5','letiep6','letiep7','letiep8')
	f = open('c:\\withpython\\thu_nhap.txt','a')
	while(tang< len(taikhoan)):
		taikhoanx = taikhoan[tang]
		print(taikhoanx)
		driver = initDriver(taikhoanx)
		driver.get('https://golike.mobi/')
		
	
		try:
			time.sleep (1)
			driver.get("https://golike.mobi/account/manager/facebook")
			time.sleep(2)
			driver.execute_script("document.getElementsByClassName('material-icons float-right d200 hand')[0].click()")
			time.sleep(1)
			driver.execute_script("document.getElementsByClassName('d-block')[9].click()")
			time.sleep(2)

		except:
			pass
		driver.get('https://golike.mobi/')
		time.sleep (1)
		while(driver.find_elements_by_tag_name("h6")[1].text.lower() == "đang cập nhật" or (driver.find_elements_by_tag_name("h6")[0].text == driver.find_elements_by_tag_name("h6")[1].text == '0 đ')):
			time.sleep (2.5)
			driver.refresh()
			time.sleep (3.5)
		tien=driver.find_elements_by_tag_name("h6")[0].text
		gantien=driver.find_elements_by_tag_name("h6")[1].text
		mat=driver.find_elements_by_tag_name("h6")[2].text

		print(taikhoanx)
		print(tien)
		print(gantien)
		print(mat)
		tien = re.sub('\đ|\.', '', tien)
		gantien= re.sub('\đ|\.', '', gantien)
		mat=re.sub('\đ|\.', '', mat)
		anchac += int(tien)
		dangduyet += int(gantien)
		thunhap += int(tien)+int(gantien)
		mattien+=int(mat)
		f.write("\n")
		f.write(taikhoanx)
		f.write("\n")
		f.write("my money is :" )
		f.write(str(tien))
		f.write("\n")
		f.write("lucky money is  :")
		f.write(str(gantien))
		f.write("\n")
		f.write("lost money is :")
		f.write(str(mat))
		f.write("\n\n\n")
		
		driver.quit()
		tang+=1
	
	try:
		playsound("c:\\withpython\\gun0.mp3",block=True)
	except:
		pass
	
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
	f.write("second=======================================================================================")
	f.write("\n")
	f.write("all of money is :")
	f.write(str(thunhap))
	f.write("\n")
	f.write("my money is :" )
	f.write(str(anchac))
	f.write("\n")
	f.write("lucky money is  :")
	f.write(str(dangduyet))
	f.write("\n")
	f.write("lost money is :")
	f.write(str(mattien))
	f.write("\n\n\n")
	f.close()
	
