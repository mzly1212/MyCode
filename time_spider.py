import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from requests_html import HTMLSession


class TimeSpider:
    """爬取动态实时时间"""
    def __init__(self):
        self.option = webdriver.EdgeOptions()
        self.option.add_argument('--headless')
        self.browser = webdriver.Edge(options=self.option)
        self.session = HTMLSession()
        self.browser.get('https://onlinealarmkur.com/clock/zh-cn/')

    def get_time(self):
        while True:
            time_str = self.browser.find_element(By.CSS_SELECTOR, 'div.fullscreen-two > div#clock').text
            print("\r", time_str, end="", flush=True)
            # time.sleep(1)


if __name__ == '__main__':
    a = TimeSpider()
    a.get_time()