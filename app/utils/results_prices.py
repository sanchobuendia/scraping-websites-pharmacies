import pandas as pd
import json
import re
import datetime
from utils.get_prices import PriceCheck

class Results:
    def __init__(self, df, path_dict):
        self.df = df
        self.path_dict = path_dict

        with open(self.path_dict, 'r') as json_file:
            self.dict_url = json.load(json_file)

    def split_and_take_first(self, text):
        '''
            A script designed for splitting a string and taking the first part.
            The function, split_and_take_first, takes a string as input and splits it based on a predefined pattern.
            It then returns the first part of the string.
        '''
        self.text = text
        pattern_to_split = r'(\d+x)'
        split_parts = re.split(pattern_to_split, text)
        return split_parts[0]

    def extract_min_price(self, text):
        '''
            A script designed for extracting the minimum price from a string.
            The function, extract_min_price, takes a string as input and extracts the minimum price based on a predefined pattern.
            It then returns the minimum price.
        '''
        self.text = text
        price_pattern = r'r\$ (\d+\,\d{2}|\d+\.\d{2})'
        prices = re.findall(price_pattern, text)
        if prices:
            prices = [float(price.replace(',', '.')) for price in prices]  # Convert to float
            return min(prices)
        else:
            return None

    def output(self, out_path):
        '''
            A script designed for creating a dataframe containing the results of the price analysis.
            The function, output, takes a dataframe as input and performs a search on specific websites based on the provided URL.
            If the URL matches predefined patterns, it utilizes shadow DOM elements for search, while on other websites, it employs standard methods.
            The script then extracts and compiles the search results into a string format.
        '''
        self.out_path = out_path
        description = []
        price = []

        for i in range(len(self.df)):

            if self.df['REDE'][i] in self.dict_url:
                resprice = PriceCheck(loja = self.df['REDE'][i], 
                                    dict_url = self.dict_url
                                    )
                res = resprice.get_price(product = self.df['APRESENTAÇÃO'][i])
                try:
                    if (res['product_price'] == '') | (res['product_price'] == 'R$ 0,00'):
                        description.append('O produto não foi encontrado')
                        price.append("0,0")     
                    else:
                        description.append(res['product_name'])
                        price.append(res['product_price'])
                except:
                    description.append('O produto não foi encontrado')
                    price.append("0,0")
            else:
                res = 'A rede não está cadastrada'
            
        self.df['product_found'] = description
        self.df['price_found'] = price
            
        self.df.to_csv(self.out_path, index=False)
        
    
