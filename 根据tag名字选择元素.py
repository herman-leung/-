from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options = options)

wd.get('https:\\cdn2.byhy.net/files/selenium/sample1.html')


#类似的，我们可以通过指定 参数为 By.TAG_NAME ，选择所有的tag名为 div的元素

elements = wd.find_elements(By.TAG_NAME,'div')
# 取出列表中的每个WebElement对象，打印输出text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容

for element in elements:
    print(element.text)
