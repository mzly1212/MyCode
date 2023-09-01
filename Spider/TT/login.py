from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json

with open("cookies.json", "r") as json_file:
    cookies = json.load(json_file)
print(cookies)
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Edge(options=option)
driver.get('http://4a.chinatowercom.cn:20000/uac_oa/ssoForUac')
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
