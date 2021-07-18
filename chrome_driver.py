import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/usr/local/bin/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('file:///Users/bdatta/Documents/play_video.html');
time.sleep(1) 
for x in range(6):
    driver.find_element_by_xpath("//button[normalize-space()='Play Video']").click()
    time.sleep(2)
time.sleep(5)
driver.quit()