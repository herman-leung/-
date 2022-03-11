from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options = options)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

#限制 选择元素的范围是id为container元素的内部。
element = wd.find_element(By.ID, 'container')

spans = element.find_elements(By.TAG_NAME,'span')

for span in spans:
    print(span.text)



#wd.quit()
