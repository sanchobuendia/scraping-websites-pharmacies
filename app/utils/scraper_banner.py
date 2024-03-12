from selenium.webdriver.common.by import By
import os
import requests
import time
from utils.utils import delete_images, driver, getImages, get_Image_generic
from settings import settings

#from utils.utils import delete_images, driver 
#from app.settings import settings

class ImageScraper:
    def __init__(self, loja, dict_url):
        self.loja = loja
        for key, value in dict_url.items():
            if key == self.loja:
                self.url = value["url"]

        self.driver = driver()

    def create_folder(self):
        '''
            A script designed for creating a folder for storing the retrieved images.
            The function, create_folder, takes no input and creates a folder for storing the retrieved images.
            The folder is created in the same directory as the script.
        '''
        if os.path.exists(f"{settings.storage_url}images"):
            delete_images(f"{settings.storage_url}images")
        else:
            os.mkdir(f"{settings.storage_url}images")

    def get_all_images(self):
        '''
            write
        '''
        self.driver.get(self.url)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(10)

        linkListFinal = []
        linkListFinal += get_Image_generic(driver = self.driver)
        self.driver.execute_script("window.scrollTo(1000, 2500);")
        time.sleep(10)
        linkListFinal += get_Image_generic(driver = self.driver)
        self.driver.execute_script("window.scrollTo(2500, 4000);")
        time.sleep(10)
        linkListFinal += get_Image_generic(driver = self.driver)
        self.driver.execute_script("window.scrollTo(4000, 6000);")
        time.sleep(10)
        linkListFinal += get_Image_generic(driver = self.driver)
        linkListFinal = list(set(linkListFinal))

        for i, url in enumerate(linkListFinal):
            if url:
                response = requests.get(url)
                with open(os.path.join(settings.storage_url, f'images/image_{i}.jpg'), 'wb') as file:
                    file.write(response.content)
        self.driver.quit()

   