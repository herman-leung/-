from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.get("https://cdn2.byhy.net/files/selenium/test2.html")

# 先找到已经选择的选项，单击一次（取消选择），再按找到需要单击的元素进行click
s_checkboxs= wd.find_elements(By.CSS_SELECTOR,'#s_checkbox input[checked=checked]')
for s in s_checkboxs:
    s.click()
from time import sleep

sleep(2)
wd.find_element(By.CSS_SELECTOR,'#s_checkbox input[value="小雷老师"]').click()



a = wd.find_element_by_css_selector("#ss_single option[selected='selected']").get_attribute("value")
print(a)
