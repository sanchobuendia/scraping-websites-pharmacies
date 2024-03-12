import os
import shutil
import glob
import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from settings import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def delete_images(folder):
    """
    Delete a folder and its content.

        Parameters
        ----------
        folder : str
        The folder path.
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def recent_file_input(folder_path):
    '''
        A script designed for extracting the most recent file in a folder.
        The function, recent_file, takes a folder path as input and returns the most recent file in the folder.
        If no files are found, the function returns None.

        Returns:
        - str: The most recent file in the folder.

        Raises:
        - None: The script handles potential errors internally and returns informative messages.
        For instance, it returns a message stating "O produto não foi encontrado" if the product is not found in the search results.
    '''
    # Create a list of all files in the folder that match the pattern
    file_list = glob.glob(os.path.join(folder_path, 'input_*.csv'))

    # Check if there are any files in the folder
    if not file_list:
        return None  # Return None if no files are found
    else:
        # Sort the list of files by modification time (most recent first)
        file_list.sort(key=os.path.getmtime, reverse=True)

        # Get the most recent file
        most_recent_file = file_list[0]

        # Extract the file name
        file_name = os.path.basename(most_recent_file)

        return file_name
    
def recent_file_output(folder_path):
    '''
        A script designed for extracting the most recent file in a folder.
        The function, recent_file, takes a folder path as input and returns the most recent file in the folder.
        If no files are found, the function returns None.

        Returns:
        - str: The most recent file in the folder.

        Raises:
        - None: The script handles potential errors internally and returns informative messages.
        For instance, it returns a message stating "O produto não foi encontrado" if the product is not found in the search results.
    '''
    # Create a list of all files in the folder that match the pattern
    file_list = glob.glob(os.path.join(folder_path, 'output_*.csv'))

    # Check if there are any files in the folder
    if not file_list:
        return None  # Return None if no files are found
    else:
        # Sort the list of files by modification time (most recent first)
        file_list.sort(key=os.path.getmtime, reverse=True)

        # Get the most recent file
        most_recent_file = file_list[0]

        # Extract the file name
        file_name = os.path.basename(most_recent_file)

        return file_name

def driver():
    '''
        A script designed for creating a webdriver instance.
        The function, driver, takes no input and returns a webdriver instance.
        The webdriver instance is created using the Firefox webdriver and the webdriver_manager package.
        The webdriver instance is configured to run in headless mode.

        Returns:
        - webdriver: A webdriver instance.

        Raises:
        - None: The script handles potential errors internally and returns informative messages.
        For instance, it returns a message stating "O produto não foi encontrado" if the product is not found in the search results.
    '''
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=firefox_options)
    return driver

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

def getImages(driver):
        linkList = []
        iframes = driver.find_elements(By.TAG_NAME, 'iframe')
        for index, iframe in enumerate(iframes):
            try:
                driver.switch_to.frame(index)

                images = driver.find_elements(By.CSS_SELECTOR, 'a > img')

                for image in images:
                    src = image.get_attribute('src')
                    linkList.append(src)

            except Exception as e:
                print(f"Erro ao processar o iframe {index}: {str(e)}")

            finally:
                driver.switch_to.default_content()
        return linkList

def get_Image_generic(driver):
    linkList = []
    try:
        time.sleep(10)
        images = driver.find_elements(By.CSS_SELECTOR, 'a > img')
        for image in images:
            src = image.get_attribute('src')
            linkList.append(src)

    except Exception as e:
        print(f"Erro ao processar o iframe: {str(e)}")

    finally:
        driver.switch_to.default_content()
    return linkList
