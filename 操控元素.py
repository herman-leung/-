from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(10)

wd.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=bilibili&fenlei=256&rsv_pq=dca872fd0002b4ae&rsv_t=b10bIosYoe9uIWHW8KRTyOL5qZEChX3dQCy3if000q9v0RaXU%2FkAHROF6lI&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=8&rsv_sug1=2&rsv_sug7=100&rsv_btype=i&inputT=5305&rsv_sug4=5305&rsv_jmp=fail&p_tk=2145z1RBE63gufH8FcjXrXCWNnBhb5pKPSEDelw4SmWyCaUMmkFdC69%2F3POixP3yRT1dq1pFrcpeJR9oJBU1AlVqS35rq%2BGXLnSlE%2FAKPX73UoqYJlhNy%2FQUMsHT5TpagGDH&p_timestamp=1647157657&p_sign=1b3c80b3bc7a79aaf084c4b10c52a3c0&p_signature=90534abf01ed895111e1f5c82cc98a6d&__pc2ps_ab=2145z1RBE63gufH8FcjXrXCWNnBhb5pKPSEDelw4SmWyCaUMmkFdC69%2F3POixP3yRT1dq1pFrcpeJR9oJBU1AlVqS35rq%2BGXLnSlE%2FAKPX73UoqYJlhNy%2FQUMsHT5TpagGDH|1647157657|90534abf01ed895111e1f5c82cc98a6d|1b3c80b3bc7a79aaf084c4b10c52a3c0')

element = wd.find_element(By.ID,'kw')
#element.send_keys('bilibili')

element.clear()
