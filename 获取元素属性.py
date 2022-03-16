from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.get('https://www.byhy.net/_files/stock1.html')

element =wd.find_element(By.ID,'suggestion')


#获取placeholder的信息。
text = element.get_attribute('placeholder')
print(text)   #一句话建议


element = wd.find_element(By.ID,'1')
#获取整个元素对应的html文本内容可以使用element.get_attribute('outerHTML')
htmlinfo = element.get_attribute('outerHTML')    #<input type="text" id="suggestion" placeholder="一句话建议" style="height: 1.2rem;">
print(htmlinfo)

#如果，只是想获取某个元素 内部 的HTML文本内容，可以使用 element.get_attribute('innerHTML')
textinfo = element.get_attribute('innerHTML')
print(textinfo)     #<p class="name">包钢股份</p>
                          #<p>代码：<span>600010</span></p>

