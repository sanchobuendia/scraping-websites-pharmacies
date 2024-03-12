import pandas as pd
import json
import os
import datetime
from settings import settings
from utils.scraper_banner import ImageScraper
from utils.match_images import MatchImages

class Results:
    def __init__(self, df, folder_path, out_path, threshold, path_dict):
        self.df = df
        self.folder_path = folder_path
        self.out_path = out_path
        self.threshold = threshold
        self.path_dict = path_dict

        with open(self.path_dict, 'r', encoding='utf8') as json_file:
            self.dict_url = json.load(json_file)

        self.df['rede_cadastrada'] = False
        self.df['imagem_enviada'] = False

    def create_output(self):
        '''
            A script designed for creating a dataframe containing the results of the image analysis.
            The function, create_output, takes a dataframe as input and performs a search on specific websites based on the provided URL.
            If the URL matches predefined patterns, it utilizes shadow DOM elements for search, while on other websites, it employs standard methods.
            The script then extracts and compiles the search results into a string format.
        '''
        farmacia = None
        for i in range(len(self.df)):
            if self.df['REDE'][i] in self.dict_url:
                self.df.loc[i, 'rede_cadastrada'] = True
                target_filename = self.df['NOME DAS IMAGENS'][i]

                for pasta_raiz, subpastas, arquivos in os.walk(self.folder_path):
                    for arquivo in arquivos:
                        if arquivo.split(".")[0] == target_filename:
                            self.df.loc[i, 'imagem_enviada'] = True
                            target_path = os.path.join(pasta_raiz, arquivo).replace("\\","/")
                            if farmacia == self.df['REDE'][i]:
                                matcher = MatchImages(folder_path=f'{settings.storage_url}images', target_path=target_path, threshold=self.threshold)
                                res_bool = matcher.match_threshold()
                                self.df.loc[i, 'MATCH'] = res_bool
                            else:
                                scraper = ImageScraper(loja=self.df['REDE'][i], dict_url = self.dict_url)

                                scraper.get_all_images()
                                    
                                matcher = MatchImages(folder_path=f'{settings.storage_url}images', target_path=target_path, threshold=self.threshold)
                                res_bool = matcher.match_threshold()
                                self.df.loc[i, 'MATCH'] = res_bool
                                farmacia = self.df['REDE'][i]
                        else:
                            pass
            else:
                pass

        self.df['validade_campanha'] = False
        
        current_date = datetime.date.today()
        self.df['DATA INICIAL'] = pd.to_datetime(self.df['DATA INICIAL']).dt.date
        self.df['DATA FINAL'] = pd.to_datetime(self.df['DATA FINAL']).dt.date
        self.df.loc[(self.df['DATA INICIAL'] <= current_date) & (self.df['DATA FINAL'] >= current_date), 'validade_campanha'] = True

        folder_path = f"{settings.storage_url}target_images"
        [os.remove(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

        self.df.to_csv(self.out_path, index=False)
        
