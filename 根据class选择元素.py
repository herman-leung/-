from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options = options)

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

# find_elements 返回所有class为plant的元素， 放在一个列表返回
'''
elements = wd.find_elements(By.CLASS_NAME, 'plant')

for element in elements:
    print(element. text)
'''
# find_element 只返回第一个class为plant的元素
#element = wd.find_element(By.CLASS_NAME,'plant')
#print(element.text)


