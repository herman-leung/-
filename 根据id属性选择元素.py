from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

 
#加上這些參數， 禁止chromedriver 寫屏

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = webdriver.Chrome(options=options)


#wd = webdriver.Chrome(service = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'))

wd.get("https://www.byhy.net/_files/stock1.html")

#element = wd.find_element_by_id('kw').send_keys('bilibili')  不建议这么写， 会警告，这是旧版写法
element = wd.find_element(By.ID, 'suggestion')
element.send_keys('bilibili')

element = wd.find_element(By. CSS_SELECTOR, 'button[id ^=submit]').click()  #一句话建议 成功执行。
