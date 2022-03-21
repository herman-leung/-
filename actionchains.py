'''
ActionChains  模拟鼠标移动等动作

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.get('https://www.baidu.com/')
ac = ActionChains(wd)
#鼠标移动到元素上

ac.move_to_element(
wd.find_element(By.CSS_SELECTOR,'a[name="tj_briicon"]')
    ).perform()


os.system("taskkill /im chromedriver.exe /F")

