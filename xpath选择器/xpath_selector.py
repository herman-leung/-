from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
import time
'''
绝对路径  /html/body/div
相对路径 如: //div//span
'''
wd = webdriver.Chrome("F:\\ChromeGo\\ChromeGo\\Browser\\chromedriver.exe")
wd.get("https://cdn2.byhy.net/files/selenium/test1.html")
'''
/html/body/div/div/div/span//*[@id='newyork']  == //*[@id='newyork']
'''
# //找到多选框,并且打印默认选中的值
elements = wd.find_elements(By.XPATH,'/html/body/div/div/div/span/p')
for e in elements:
    print(e.text)



