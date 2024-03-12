from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#from utils.utils import driver, scrape_product_info, search_product
from utils.getpricesutils import search_product_araujo, search_product_drogal, search_product_drogasmil, search_product_dsp, search_product_extrafarma, search_product_globo, search_product_nissei, search_product_pacheco, search_product_paguemenos, search_product_panvel, search_product_rosario, search_product_tamoio, search_product_indiana, search_product_sj, search_product_catarinense, search_product_precopopular, search_product_venancio

class PriceCheck:
    def __init__(self, loja, dict_url):
        self.loja = loja

        for key, value in dict_url.items():
            if key == self.loja:
                self.url = value["url"]

    def get_price(self, product):
        '''
            A web scraping script designed for retrieving product prices from various online pharmacy websites.
            The function, get_price, takes a product as input and performs a search on specific websites based on the provided URL.
            If the URL matches predefined patterns, it utilizes shadow DOM elements for search, while on other websites, it employs standard methods.
            The script then extracts and compiles the search results into a string format.

            Returns:
            - str: A string containing the retrieved product prices or a message indicating that the product was not found.

            Raises:
            - None: The script handles potential errors internally and returns informative messages.
            For instance, it returns a message stating "O produto não foi encontrado" if the product is not found in the search results.
        '''
        self.product = product
            
        if (self.url == "https://www.araujo.com.br/"):
            araujo = search_product_araujo(product = self.product
                                    )
             
            return araujo
        elif (self.url == "https://www.drogal.com.br/"):
            drogal = search_product_drogal(product = self.product, 
                                    url = "https://www.drogal.com.br/",
                                    searchHeader = "q")
             
            return drogal
        elif (self.url == "https://www.drogasmil.com.br/"):
            drogasmil = search_product_drogasmil(product = self.product
                                    )
             
            return drogasmil
        elif (self.url == "https://www.drogariasaopaulo.com.br/"):
            drogariasaopaulo = search_product_dsp(product = self.product
                                    )
             
            return drogariasaopaulo
        elif (self.url == "https://www.extrafarma.com.br/"):
            extrafarma = search_product_extrafarma(product = self.product
                                    )
             
            return extrafarma
        elif (self.url == "https://www.drogariaglobo.com.br/"):
            drogariaglobo = search_product_globo(product = self.product
                                    )
             
            return drogariaglobo
        elif (self.url == "https://www.farmaciasnissei.com.br/"):
            drogarianissei = search_product_nissei(product = self.product
                                    )
             
            return drogarianissei
        
        elif (self.url == "https://www.drogariaspacheco.com.br/"):
            drogariapacheco = search_product_pacheco(product = self.product
                                    )   
             
            return drogariapacheco
        
        elif (self.url == "https://www.paguemenos.com.br/"):
            paguemenos = search_product_paguemenos(product = self.product
                                    )
             
            return paguemenos
        elif (self.url == "https://www.panvel.com/"):
            panvel = search_product_panvel(product = self.product
                                    )
            return panvel
        elif (self.url == "https://www.drogariarosario.com.br/"):
            rosario = search_product_rosario(product = self.product
                                    )
            return rosario
        elif (self.url == "https://www.drogariastamoio.com.br/"):
            tamoio = search_product_tamoio(product = self.product
                                    )
            return tamoio
        elif (self.url == "https://www.farmaciaindiana.com.br/"):
            venancio = search_product_indiana(product = self.product
                                    )
            return venancio
        elif (self.url == "https://www.saojoaofarmacias.com.br/"):
            sj = search_product_sj(product = self.product
                                    )
            return sj
        elif (self.url == "https://www.drogariacatarinense.com.br/"):
            catarinense = search_product_catarinense(product = self.product
                                    )
            return catarinense
        
        elif (self.url == "https://www.precopopular.com.br/"):
            preco = search_product_precopopular(product = self.product
                                    )
            return preco
        elif (self.url == "https://www.drogariavenancio.com.br/"):
            ven = search_product_venancio(product = self.product
                                    )
            return ven
        
        
        
        
            
            
        



   
