from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
import time

def initDriver(filePath):
	options = webdriver.ChromeOptions()
	options.add_argument(r'user-data-dir=E:\Users\tiep\OneDrive\Máy tính\withpython\tiep')
	#config ko load anh
	'''
	prefs = {
	"profile.managed_default_content_settings.images": 2
	}
	chrome_options.add_experimental_option("prefs", prefs)
	'''
	
	browser = webdriver.Chrome(executable_path=r"E:\Users\tiep\OneDrive\Máy tính\withpython\chromedriver.exe", chrome_options=options)
	return browser 

def ham_surf_face(filePath):
	
	driver=initDriver(filePath)
	driver.get('https://www.facebook.com/')
	#wait khi story xuat hien <=> load success
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#stories_tray")))
	
	count_eles_btn_like=0

	while(True):
		#scroll down
		driver.execute_script("window.scrollBy(0,0.7*window.innerHeight)")
		time.sleep(2)

		eles_btn_like=driver.find_elements_by_css_selector('div[data-testid="UFI2ReactionLink/actionLink"] a')
		count_eles_btn_like=len(eles_btn_like)
		#eles_btn_like[0].click()
		print(count_eles_btn_like)

def pool_handler():
	p = Pool(2)
	
	kq=p.map_async(ham_surf_face, ('chrome','chrome2'))
	print('main')
	print(kq.get())
	p.close()
	p.join()
	print('Task ended. Pool join.')


if __name__ == '__main__':
    pool_handler()


    find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector