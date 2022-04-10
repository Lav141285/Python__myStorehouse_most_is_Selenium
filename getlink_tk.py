
from selenium import webdriver
import time

def initDriver(filepath):
    options = webdriver.ChromeOptions()
    options.add_argument(r'user-data-dir=c:\\withpython\\account_facebook\\'+ filepath)
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    prefs = {
    "profile.managed_default_content_settings.images":2
    }
    
    options.add_experimental_option("prefs",prefs)
    
    driver = webdriver.Chrome(executable_path=r'c:\\withpython\\chromedriver.exe', options=options)
    return driver


tang=0
if __name__ == '__main__':
    link=[]
    while(1):
        taikhoan =  ('tieple247','tieple02','happier_in_2021_1','happier_in_2021_2','happier_in_2021_3','happier_in_2021_4','happier_in_2021_5','happier_in_2021_6','happier_in_2021_7','happier_in_2021_8','happier_in_2021_9')

        if((tang) > len(taikhoan)-1):
            break
        taikhoanx = taikhoan[tang]
        print (taikhoanx)
        driver = initDriver(taikhoanx)

        driver.get("https://golike.mobi/account/manager/facebook")
        time.sleep(1)
        driver.execute_script("document.getElementsByClassName('material-icons float-right d200 hand')[0].click()")
        link.append(driver.find_elements_by_class_name('d-block')[10].get_attribute('href'))

        driver.quit()
        
        tang+=1
    f=open("C:\\withpython\\linkfb.txt","w")
    for i in link:
        f.write(i)
        f.write('\n')
    f.close()