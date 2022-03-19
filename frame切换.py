from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)

#wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

'''

※※※

切换到iframe中查找， 参数可以说iframe的name也可以是id
也可以填写frame 所对应的 WebElement 对象。
即： wd.switch_to.frame(wd.find_element(By.TAG_NAME,'iframe')
 
'''
#wd.switch_to.frame('innerFrame')
wd.switch_to.frame(wd.find_element(By.TAG_NAME,'iframe'))

elements = wd.find_elements(By.CLASS_NAME, 'plant')
for element in elements:
    print(element.text)
    with open('a.txt', 'a') as f:
        f.write(element.text)

'''
当需要操作主html时， 要切换回主html。
wd.switch_to.default_content()
'''

wd.switch_to.default_content()
key = wd.find_element(By.ID,'outerbutton')
for i in range(1,5):
    key.click()
    time.sleep(2)
wd.quit()
