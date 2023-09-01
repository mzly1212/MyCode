import json, time
# import socket
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver


class Web:

    def __init__(self):
        self.option = webdriver.EdgeOptions()
        self.option.add_experimental_option("detach", True)
        self.browser = webdriver.Edge(options=self.option)

    def start(self):
        self.browser.get('http://4a.chinatowercom.cn:20000/uac/login')
        input('确认登录...')
        self.browser.refresh()
        time.sleep(5)
        cookies_ = self.browser.get_cookies()
        return cookies_

    def saveCookies(self, cookies):
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

if __name__ == '__main__':
    a = Web()
    cookies = a.start()
    print(cookies)
    a.saveCookies(cookies)
