from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import requests
from PIL import Image, ImageChops
import time
import cv2
import numpy as np
import glob
import shutil
from utils import delete_images
from skimage import io
from skimage.metrics import structural_similarity as compare_ssim

class ImageScraper:
    def __init__(self, loja, dict_url):
        self.loja = loja

        for key, value in dict_url.items():
            if key == self.loja:
                self.url = value["url"]
                self.dom = value["dom"]
                self.css_result = value["css_result"]
                self.searchbox = value["searchbox"]
                self.searchresults = value["searchresults"]
                self.banner_xpath = value["banner_xpath"]
                self.url_category = value["url_category"]
                self.category_xpath = value["category_xpath"]
                self.urlsubcategory = value["urlsubcategory"]
                self.subcategory_xpath = value["subcategory_xpath"]
                self.carousel_button_xpath = value["carousel_button_xpath"]
                self.cookie_button_css = value["cookie_button_css"]
                self.iframe_css = value["iframe_css"]
                self.banner_xpath = value["banner_xpath"]

        # set Firefox driver options
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

    def get_banners(self, page):
        self.page = page

        if os.path.exists("images"):
            delete_images("images")
        else:
            os.mkdir("images")

        if self.page == "pagina principal":
            self.driver.get(self.url)
        else:
            self.driver.get(self.searchbox)

        time.sleep(60)

        if self.cookie_button_css != " ":
            self.driver.find_element(By.CSS_SELECTOR, self.cookie_button_css).click()
            time.sleep(22)

        if "medicamentos" in self.url or "drogariaglobo" in self.url:
            if self.carousel_button_xpath != " ":
                for i in range(12):
                    self.driver.find_element(By.XPATH, self.carousel_button_xpath).click()
                    time.sleep(2)

        container = self.driver.find_element(By.XPATH, self.banner_xpath)
        images = container.find_elements("css selector",'img')

        for i, image in enumerate(images):
            image_url = image.get_attribute("src")
            if image_url is None or image_url == '' or 'data:image/svg+xml' in image_url or ".svg" in image_url or 'data:image/gif' in image_url:
                pass
            else:
                time.sleep(1)
                response = requests.get(image_url)
                with open(f"images/image_{i}.jpg", "wb") as f:
                    f.write(response.content)

        self.driver.quit()


    def get_images_iframe(self):

        self.driver.get(self.url)
        time.sleep(6)
        if self.cookie_button_css != False:
            self.driver.find_element(By.CSS_SELECTOR, self.cookie_button_css).click()
            time.sleep(2)

        # navigate to the website
        for iframe_number in range(5,8):
            self.driver.get(self.url)
            time.sleep(6)

            try:
                if iframe_number == 8:
                    pass

                else:
                    if self.iframe_css != False:
                        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, self.iframe_css+str(iframe_number)))
                        time.sleep(2)

                    container = self.driver.find_element(By.XPATH, self.category_xpath)
                    images = container.find_elements("css selector",'img')

                    if os.path.exists("images"):
                        delete_images("images")
                    else:
                        os.mkdir("images")

                    for i, image in enumerate(images):
                        image_url = image.get_attribute("src")
                        if image_url == None or image_url == '' or 'data:image/svg+xml' in image_url or ".svg" in image_url or 'data:image/gif' in image_url or '/_next/image?url=' in image_url:
                            pass
                        else:
                            time.sleep(1)
                            response = requests.get(image_url)
                            with open(f"images/image_{iframe_number}.jpg", "wb") as f:
                                f.write(response.content)
            except Exception as error:
                # handle the exception
                print("An exception occurred:", error)
        self.driver.quit()


    def url_ache_mosaic(self):
        """
        To get mosaic images from an url.

            Parameters
            ----------
            url : str
                The url that will be accessed.
            category_xpath : str
                DOM Xpath from the banner.
        """    
        self.driver.get(self.url)

        time.sleep(30)

        container = self.driver.find_element(By.XPATH, self.category_xpath)
        images = container.find_elements("css selector",'img')

        if os.path.exists("images"):
            delete_images("images")
        else:
            os.mkdir("images")

        for i, image in enumerate(images):
            image_url = image.get_attribute("data-src")
            if image_url == None or image_url == '' or 'data:image/svg+xml' in image_url or ".svg" in image_url or 'data:image/gif' in image_url:
                pass
            else:
                image_url = self.url + image.get_attribute("data-src")
                time.sleep(1)
                response = requests.get(image_url)
                with open(f"images/image_{i}.jpg", "wb") as f:
                    f.write(response.content)

        self.driver.quit()
    
# Example usage of the ImageScraper class
if __name__ == "__main__":
    scraper = ImageScraper(loja="your_url_here")
    scraper.get_images_from_banner()
