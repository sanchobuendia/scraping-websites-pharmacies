import pandas as pd
import json
import re
from get_prices import PriceCheck

class Results:
    def __init__(self, df, dict_url, openai_api_key, openai_api_base, openai_api_version):
        self.df = df
        self.dict_url = dict_url
        self.openai_api_key = openai_api_key
        self.openai_api_base = openai_api_base
        self.openai_api_version = openai_api_version

    def split_and_take_first(self, text):
        self.text = text
        pattern_to_split = r'(\d+x)'
        split_parts = re.split(pattern_to_split, text)
        return split_parts[0]

    def extract_min_price(self, text):
        self.text = text
        price_pattern = r'r\$ (\d+\,\d{2}|\d+\.\d{2})'
        prices = re.findall(price_pattern, text)
        if prices:
            prices = [float(price.replace(',', '.')) for price in prices]  # Convert to float
            return min(prices)
        else:
            return None

    def output(self):
        description = []
        name_found = []
        price_found = []
        for i in range(len(self.df)):
            resprice = PriceCheck(loja = self.df.iloc[i, 0], 
                                dict_url = self.dict_url,
                                openai_api_key = self.openai_api_key, 
                                openai_api_base = self.openai_api_base,
                                openai_api_version= self.openai_api_version)
            res = resprice.get_price(product = self.df.iloc[i, 6])
            description.append(res)
            #name_found, precos = resprice.extract_price_openai(res)
            #name_found.append(name_found)
            #price_found.append(precos)
        
        self.df['descricao'] = description
        self.df['descricao2'] = self.df['descricao'].str.replace('\n', ' ')
        self.df['descricao2'] = self.df['descricao2'].str.replace('R$ ', 'R$')
        self.df['descricao2'] = self.df['descricao2'].str.replace('R$', 'R$ ')
        self.df['descricao2'] = self.df['descricao2'].str.lower()
        self.df['descricao2'] = self.df['descricao2'].apply(self.split_and_take_first)
        self.df['price_found'] = self.df['descricao2'].apply(self.extract_min_price)

        self.df = self.df.drop('descricao2', axis=1)
        self.df['match'] = False
        self.df.loc[self.df['price_found'] == self.df['price_found'], 'match'] = True


        #df['nome encontrado'] = name_found
        #df['preço encontrado'] = price_found

        return self.df