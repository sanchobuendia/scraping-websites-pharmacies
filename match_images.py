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


class MatchImages:
    def __init__(self, folder_path, target_path, threshold):
        self.folder_path = folder_path
        self.target_path = target_path
        self.threshold = threshold

    def match_threshold(self):
        for filename in os.listdir(self.folder_path):
            pathf = os.path.join(self.folder_path, filename)
            # Carregar as imagens
            img1 = io.imread(pathf)
            img2 = io.imread(self.target_path)

            # Verificar se as imagens foram carregadas corretamente
            # if img1 is None or img2 is None:
            #    raise ValueError("Não foi possível carregar as imagens.")

            # Converter as imagens para tons de cinza (para comparar melhor)
            gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            if gray_img1.shape != gray_img2.shape:
                gray_img1 = cv2.resize(
                    gray_img1, (gray_img2.shape[1], gray_img2.shape[0])
                )

            # Calcular o coeficiente de similaridade estrutural (SSIM) entre as imagens
            ssim = compare_ssim(gray_img1, gray_img2)

            # Se o valor SSIM for maior que o limite, as imagens são consideradas iguais
            if ssim > self.threshold:
                return True
            else:
                pass
        return False


# Example usage of the ImageScraper class
if __name__ == "__main__":
    scraper = MatchImages(
        folder_path="folder_path",
        target_path="image_target_path",
        threshold="threshold",
    )
    scraper.match_threshold()
