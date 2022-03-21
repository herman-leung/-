from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

select = Select(wd.find_element(By.ID,'ss_multi'))

# 清除所有 已经选中 的选项
select.deselect_all()

#根据文本 选择小雷老师 小江老师
select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小江老师')
sleep(3)

'''
#去除掉某个选项  index从0开始
select.deselect_by_index(0)
deselect_by_value根据选项的value属性值， 去除 选中元素
deselect_by_visible_text根据选项的可见文本，去除 选中元素

'''
select.deselect_by_value('小雷老师')
#kill掉chromedriver进程
os.system('taskkill /im chromedriver.exe /F')
