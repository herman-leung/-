from selenium import webdriver
from selenium.webdriver.common.by import By
import time



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(10)

wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID,'kw')
element.send_keys('通讯')
element = wd.find_element(By.CSS_SELECTOR, 'button[id=go]')
element.click()


#time.sleep(1)  #程序太快， 网页响应慢，需要等待一会儿

'''
while True:
    try:
        element = wd.find_element(By.ID,'1')
        print(element.text)
        break;
    except:
        time.sleep(1) #休息一下，防止耗cpu
'''
'''
二：
    selenium 为我们提供了 隐式等待的解决方案
    当发现元素没有找到的时候，并不立即返回找不到的元素的错误
    而是周期性（每隔半秒钟）重新寻找该元素，直到该元素找到。
    或者超出指定最大等待时长，这时才抛出异常（如果是find_elements之类的方法，则是返回空列表）
    selenium的webdriver对象有个方法叫implicitly_wait, 接受一个参数，指定最大等待时长
'''


element = wd.find_element(By.ID,'1')
print(element.text)

wd.quit()
