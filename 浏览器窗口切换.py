from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

wd=webdriver.Chrome(options=options)

wd.get("https://cdn2.byhy.net/files/selenium/sample3.html")

elements = wd.find_element(By.TAG_NAME,'a')

elements.click()


#print(wd.title)
'''
上行代码 输出内容是白月黑羽测试网页3,这说明，webdriver对象指向的还是老窗口
'''

mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    #先切换到该窗口
    wd.switch_to.window(handle)
    #得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        #如果是，当前webdriver对象指向的就是对应的窗口，此时，跳出循环
        break;
print(wd.title)

'''
同样的，如果我们在新窗口 操作结束后， 还要回到原来的窗口，该怎么办？

我们可以仍然使用上面的方法，依次切入窗口，然后根据 标题栏 之类的属性值判断。

还有更省事的方法。

因为我们一开始就在 原来的窗口里面，我们知道 进入新窗口操作完后，还要回来，可以事先 保存该老窗口的 句柄，使用如下方法
'''
# mainWindow变量保存当前窗口的句柄
#mainWindow = wd.current_window_handle

#切换到新窗口操作完后，就可以直接像下面这样，将driver对应的对象返回到原来的窗口
#通过前面保存的老窗口的句柄，自己切换到老窗口
wd.switch_to.window(mainWindow)
button = wd.find_element(By.ID, 'outerbutton')
button.click()
