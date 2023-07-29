from PIL import Image
import time, os, threading
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def check_image(img_path):
    try:

        # 打开图片并检测是否损坏
        img = Image.open(img_path)
        img.verify()
        img.close()
        # print("图片正常")
        return True

    except:
        print("图片损坏")
        img.close()
        os.remove(img_path)  # 删除损坏的图片
        return False


class BS_spider:
    """bright sky"""

    def __init__(self, save_path):
        self.option = webdriver.EdgeOptions()
        self.prefs = {'profile.default_content_settings.popups': 0,
                      'download.default_directory': r'D:\Python-Code\Spider\imgs'}
        # self.option.add_experimental_option("detach", True)
        # self.option.add_experimental_option('prefs', self.prefs)
        self.option.add_argument("--headless")
        self.browser = webdriver.Edge(options=self.option)
        self.save_path = save_path
        self.session = HTMLSession()


    def getZipDataFromGoogleLinks(self, links):
        for link in links:
            fileId = link.strip().split('/file/d/')[-1].split('/view?')[0]
            downloadUrl = f'https://drive.google.com/uc?id={fileId}&export=download'
            self.browser.get(downloadUrl)
            zipUrl = self.browser.find_element(By.CSS_SELECTOR, '#download-form').get_attribute('action')
            zipFile = self.browser.find_element(By.CSS_SELECTOR, '#uc-text > p.uc-warning-subcaption > span > a').text
            cookies = {
                "Cookie": "1P_JAR=2023-07-26-10; AEC=Ad49MVFMQMZcD948dWCVSVKw1nlvdE3M-VYoTdWdfAcs_677kX8mz5bYKQ; NID=511=uyULV_o5VkEfNSl9ZhnqjFcnPA06cCZR3MN1a_i7rSFMroMpkYSweEiaTfkl1EiYP28nmbPHAaslen2R44v1Caze5h7W0g2BcrX1HDENTpsbpuvKEEOSgBBLFeS9vazGem9ajsuKuOOKGWWrC91VM3D6e1sgOdQCfKX3PY6Hyw0M2uJZB1DAlGWAKfNqFsSZF0X1CMenuNCMFAXOmiQ"}
            with open(self.savePath(zipFile), 'wb') as f:
                while True:
                    try:
                        res = self.session.get(zipUrl, cookies=cookies).content
                        f.write(res)
                        break
                    except:
                        print(f'{zipFile} > 错误, 重试......')
                print(f'{zipFile} > 下载完成')

    def savePath(self, file):
        file_path = os.path.join(self.save_path, file)
        if os.path.exists(file_path):
            file_name, file_ext = os.path.splitext(file)
            count = 1
            while os.path.exists(file_path):
                new_file_name = f'{file_name}{count}{file_ext}'
                file_path = os.path.join(self.save_path, new_file_name)
                count += 1
        return file_path

    def getPostImgUrls(self, url):
        self.browser.get(url)
        folderName = self.browser.find_element(By.CSS_SELECTOR,
                                               '#page > header > div.post__info > h1 > span:nth-child(1)').text
        folder_path = os.path.join(self.save_path, folderName)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        img_nodes = self.browser.find_elements(By.CSS_SELECTOR,
                                               'div.post__body > div.post__files > div.post__thumbnail > a')
        img_urls = []
        for node in img_nodes:
            img_url = node.get_attribute('href')
            img_urls.append(img_url)
        return img_urls, folder_path

    def downloadImgs(self, imgUrls, folder_path, index):
        # print(folder_path.split("\\")[-1], ' ===>>> 开始下载')
        for i, imgUrl in enumerate(imgUrls):

            img_ext = imgUrl.split('.')[-1]
            i += index
            img_path = os.path.join(folder_path, f'{str(i)}.{img_ext}')
            with open(img_path, 'wb') as f:
                while True:
                    try:
                        # cookies = {"Cookie": "__ddg1_=1ygPIVjRXjh1G0gKdz83; session=eyJfcGVybWFuZW50Ijp0cnVlLCJhY2NvdW50X2lkIjo0NzI2MzF9.ZL8dkg.xPtMY2AjCo_YdZ1QWfkSkrnoDCA"}
                        data = self.session.get(imgUrl).content
                        f.write(data)
                        f.close()
                        if check_image(img_path):
                            break
                    except:
                        print(f'{str(i)}.{img_ext}连接错误，重试......')
                print(f'{str(i)}.{img_ext} > 下载完成')
        # print(folder_path.split("\\")[-1], ' > 下载完成')

    def use3ThreadToDownload(self, post_url):
        img_urls, folder_path = self.getPostImgUrls(post_url)
        num = len(img_urls)
        # print(num)
        a1 = img_urls[:int(num / 3)]
        a2 = img_urls[int(num / 3):int(num * 2 / 3)]
        a3 = img_urls[int(num * 2 / 3):]
        print(folder_path.split("\\")[-1], f' ===>>> 开始下载, 共{num}张')
        threading.Thread(target=self.downloadImgs, args=(a1, folder_path, 0)).start()
        threading.Thread(target=self.downloadImgs, args=(a2, folder_path, int(num / 3))).start()
        threading.Thread(target=self.downloadImgs, args=(a3, folder_path, int(num * 2 / 3))).start()


if __name__ == '__main__':
    path = r'D:\aCS'
    aa = BS_spider(path)
    post_url = 'https://kemono.party/fanbox/user/35688828/post/5642337'
    aa.use3ThreadToDownload(post_url)