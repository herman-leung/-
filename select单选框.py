#https://www.w3school.com.cn/tags/att_select_multiple.asp
#查看select标签mutiple属性



'''
Selenium专门提供了一个Select类进行操作

'''
from selenium import webdriver
from selenium.webdriver.common.by import By


#导入Select类
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)

wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

select = Select(wd.find_element(By.ID,'ss_single'))

select.select_by_visible_text('小江老师')

import os


# 关闭chromedriver.exe 进程
os.system('taskkill /im chromedriver.exe /F')

#关闭chrome浏览器
#os.system('taskkill /im chrome.exe /F')
#print("end")
