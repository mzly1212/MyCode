from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from requests_html import HTMLSession
import time
import os

prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': r'E:\cs'}

# 不自动关闭浏览器
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
option.add_experimental_option('prefs', prefs)
s = HTMLSession()
url = 'https://kemono.party/patreon/user/87754600/post/82837217'
driver = webdriver.Edge(options=option)
driver.get(url)
# print(driver.page_source)
img_nodes = driver.find_elements(By.CSS_SELECTOR, 'a.fileThumb.image-link')
img_urls = []
for node in img_nodes:
    img_url = node.get_attribute('href')
    img_urls.append(img_url)
# print(len(img_urls), img_urls)
root = r'E:\cs'
for i, url in enumerate(img_urls):
    img_name = url.split('/')[-1].split('?')[0]
    with open(os.path.join(root, str(i)+'.png'), 'wb') as f:
        while True:
            try:
                img_data = s.get(url=url)
                f.write(img_data.content)
                print(f'{img_name}  ===>>   下载完成！！！')
                break  # 成功下载后跳出循环
            except :
                print(f'链接失败，重试.....')
                continue


