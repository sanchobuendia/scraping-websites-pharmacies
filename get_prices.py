from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import pandas as pd
import numpy as np
import os
import openai


class PriceCheck:
    def __init__(
        self, loja, dict_url, openai_api_key, openai_api_base, openai_api_version
    ):
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

        # self.openai.api_type = "azure"
        # self.openai.api_key = openai_api_key
        # self.openai.api_base = openai_api_base
        # self.openai.api_version = openai_api_version

    def get_price(self, product):
        self.product = product
        """
        Função para buscar o preço do produto no self.url da drogaria
        """
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        # firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
        # self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        self.driver = webdriver.Firefox(options=firefox_options)

        if (
            (self.url == "https://www.drogariavenancio.com.br/")
            | (self.url == "https://www.precopopular.com.br/")
            | (self.url == "https://www.drogariacatarinense.com.br/")
        ):
            self.driver.get(f"{self.searchbox}{self.product}")
            time.sleep(10)
            shadow_host2 = self.driver.find_element(By.CSS_SELECTOR, self.dom)
            shadow_root2 = self.driver.execute_script(
                "return arguments[0].shadowRoot", shadow_host2
            )
            search_results = shadow_root2.find_elements(
                By.CSS_SELECTOR, self.css_result
            )

            if len(search_results) > 0:
                res = [x.text for x in search_results]
                res = " ".join(res)
                self.driver.quit()
                return res
            else:
                res = "O produto não foi encontrado"
                self.driver.quit()
                return res
        else:
            self.driver.get(f"{self.searchbox}{product}")
            time.sleep(10)
            search_results = self.driver.find_elements(By.XPATH, self.searchresults)

            if len(search_results) > 0:
                res = [x.text for x in search_results]
                res = " ".join(res)
                self.driver.quit()
                return res
            else:
                res = "O produto não foi encontrado"
                self.driver.quit()
                return res

    def extract_price_openai(self, description: str):
        """
        Função para extrair o nome e o preço do medicamento no texto usando a API do OpenAI
        """

        prompt = f"""Rosuvastatina Cálcica 20mg Genérico Medley 30 Comprimidos Revestidos\n46% OFF\nR$ 88,16\nR$ 48,09\nVER DESCONTOS CONVÊNIO
                            nome: Rosuvastatina Cálcica 20mg Genérico Medley 30 Comprimidos
                            preço: R$ 48,09
                            Rosuvastatina Calcica 20mg 30 Comprimidos Revestidos Althaia Generico\nALTHAIA\nR$ 79,16\nR$ 42,19
                            nome: Rosuvastatina Calcica 20mg 30 Comprimidos
                            preço: R$ 42,19
                            68%\nLeve 3 Pague 2\nLeve 3 Pague 2\nCampeão de vendas\nDesconto de laboratório\nRosuvastatina Cálcica 10mg Ranbaxy Génerico 30 Comprimidos\nR$ 21,89\nou 10x de R$ 2,18\nADICIONAR AO CARRINHO
                            nome: Rosuvastatina Cálcica 10mg Ranbaxy Génerico 30 Comprimidos
                            preço: R$ 21,89
                            R$105,36\nR$84,99\nRubia 75mcg com 84 Comprimidos
                            nome: Rubia 75mcg com 84 Comprimidos
                            preço: R$ 84,99
                            Extraia o nome e o preço do medicamento no seguinte texto: {description}"""

        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo", messages=[{"role": "user", "content": prompt}]
        )
        name_found = (
            response["choices"][0]["message"]["content"]
            .split(":")[1]
            .split("\n")[0]
            .strip()
        )
        precos = response["choices"][0]["message"]["content"].split(":")[2].strip()

        return name_found, precos
