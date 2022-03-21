from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

wd = webdriver.Chrome(options = options)

wd.get("https://cdn2.byhy.net/files/selenium/test2.html")


#选择单选框中默认选中的选项，打印出value值
element = wd.find_element(By.CSS_SELECTOR,'#s_radio input[checked = checked]')
print(element.get_attribute('value'))

sleep(3)
#自动点选小雷老师，
wd.find_element(By.CSS_SELECTOR,'input[value="小雷老师"]').click()
