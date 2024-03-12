import os
import cv2
from skimage import io
from skimage.metrics import structural_similarity as compare_ssim
from utils.utils import delete_images

class MatchImages:
    def __init__(self, folder_path, target_path, threshold):
        self.folder_path = folder_path
        self.target_path = target_path
        self.threshold = threshold

    def match_threshold(self):
        '''
            A script designed for comparing images and determining if they are similar based on a threshold value.
            The function, match_threshold, takes a folder path, a target path, and a threshold value as input.
            It then compares the images in the folder to the target image and returns a boolean value indicating whether the images are similar or not.

            Returns:
            - bool: A boolean value indicating whether the images are similar or not.

            Raises:
            - None: The script handles potential errors internally and returns informative messages.
            For instance, it returns a message stating "O produto não foi encontrado" if the product is not found in the search results.
        '''
        
        for filename in os.listdir(self.folder_path):
            try:
                pathf = os.path.join(self.folder_path, filename)
                img1 = io.imread(pathf)
                img2 = io.imread(self.target_path)

                gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

                if gray_img1.shape != gray_img2.shape:
                    gray_img1 = cv2.resize(gray_img1, (gray_img2.shape[1], gray_img2.shape[0]))

                ssim = compare_ssim(gray_img1, gray_img2)

                if ssim > self.threshold:
                    return True
                else:
                    pass
            except:
                pass
        return False
    
