from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from requests_html import HTMLSession
import time, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JeridLinksSpider:
    """爬取所有链接视频"""

    def __init__(self):
        self.option = webdriver.EdgeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': r'D:\Python-Code\Spider\imgs'}
        self.option.add_experimental_option("detach", True)
        self.option.add_experimental_option('prefs', prefs)
        self.option.add_argument("--headless")
        self.browser = webdriver.Edge(options=self.option)

        self.session = HTMLSession()

        self.links = []

    def get_links(self):
        with open('otherlinks.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            link = line.split(' : ')[-1].strip()
            self.links.append(link)

    def getVideoData(self, headers):

        url = 'https://gfs440n010.userstorage.mega.co.nz/dl/nSuG5e1m-5Jdfwd3uX0lssIKjx1uHJE76rQsXa_eBNR9U9Cwn2CNhupzonja-qdX5gXTuWBOhXVznlaoPh1RCx9Y1dpbYJlAgujLGiQ9C0JljlU8LrjREgyETFjkhg/0-4194303'
        data = self.session.post(url=url, headers=headers)
        print(data.status_code)


if __name__ == '__main__':
    a = JeridLinksSpider()
    headers_str = """Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Length: 0
Host: gfs440n010.userstorage.mega.co.nz
Origin: https://mega.nz
Referer: https://mega.nz/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
sec-ch-ua: "Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"
sec-ch-ua-platform: "Windows"
sec-ch-ua-mobile: ?0"""
    headers = {i.split(': ')[0] : i.split(': ')[1] for i in headers_str.split('\n')}
    a.getVideoData(headers=headers)