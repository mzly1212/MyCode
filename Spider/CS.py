from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from requests_html import HTMLSession
import time, os
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# option = webdriver.EdgeOptions()
# prefs = {'profile.default_content_settings.popups': 0,
#          'download.default_directory': r'D:\Python-Code\Spider\imgs'}
# option.add_experimental_option("detach", True)
# option.add_experimental_option('prefs', prefs)
# # option.add_argument("--headless")
# browser = webdriver.Edge(options=option)
#
# url = 'https://kemono.party/fanbox/user/35688828/post/5922008'
# browser.get(url)
# content = browser.find_element(By.CSS_SELECTOR, '#page > div > div.post__content > pre').text
# fileId = content.split('/d/')[-1].split('/view?')[0]
# download_url = f'https://drive.google.com/uc?id={fileId}&export=download'
# browser.get(download_url)
# browser.find_element(By.CSS_SELECTOR, '#uc-download-link').click()

def check_image(save_path):
    try:

        # 打开图片并检测是否损坏
        img = Image.open(save_path)
        img.verify()
        img.close()

        print("图片正常")
        return True

    except (IOError, SyntaxError) as e:
        print("图片损坏，重新下载")
        # os.remove(save_path)  # 删除损坏的图片
        return False
path = r'D:\CS\Barbara Sex #2 (30P)\20.jpg'
check_image(path)