# selenium-
[白月黑羽](https://www.byhy.net/tut/auto/selenium/01/)

selenium学习
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#创建webdriver实例对象， 指明使用chrome浏览器驱动
webdriver.Chrome() #括号内是chromedriver的地址， 是selenium3.x老版本写法， 新版本参照白月黑羽教程


```
```python
driver.find_element_by_link_text('登录豆瓣').click()


html = driver.page_source  #获取网页源代码
```
[python＋selenium控制浏览器在后台运行](https://xw.qq.com/amphtml/20220313A04LWB00)

[爬虫之selenium控制浏览器执行js代码](https://blog.csdn.net/weixin_44799217/article/details/112971735)

[JS代码获取网页宽高](https://www.cnblogs.com/mengshenshenchu/p/6666300.html)
f
