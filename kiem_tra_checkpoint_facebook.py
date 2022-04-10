
from selenium import webdriver
import time

def initDriver():
    options = webdriver.ChromeOptions()
    # options.add_argument(r'user-data-dir=c:\\withpython\\account_facebook\\old\\tieple03')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.headless = True
    prefs = {
    "profile.managed_default_content_settings.images":2
    }
    
    options.add_experimental_option("prefs",prefs)
    
    driver = webdriver.Chrome(executable_path=r'c:\\withpython\\chromedriver.exe', options=options)
    return driver


tang=0
if __name__ == '__main__':
    f = open("C:\\withpython\\linkfb.txt","r")
    link=f.readlines()
    f.close()
    error = open("C:\\withpython\\fbdie.txt","w")
    driver = initDriver()
    stt = 0
    while(stt< len(link)):
    
        driver.get(link[stt])
        time.sleep(1)
        
        if(len(driver.find_elements_by_tag_name('strong')) < 2):
            error.write(str(stt))
            error.write("\n")
        
        stt+=1
    error.close()
    driver.quit()
