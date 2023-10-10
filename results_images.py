import pandas as pd
import json
from scraper_banner import ImageScraper
from match_images import MatchImages
import os

class Results:
    def __init__(self, df, folder_path, threshold, dict_url):
        self.df = df
        self.folder_path = folder_path
        self.threshold = threshold
        self.dict_url = dict_url

    def create_output(self):
        for i in range(len(self.df)):
            scraper = ImageScraper(loja=self.df.iloc[i, 0], dict_url=self.dict_url)
            if self.df.iloc[i,2] == "pagina principal":
                scraper.get_banners(page = "pagina principal")
                target_path = os.path.join(self.folder_path, self.df.iloc[i, 3])
                matcher = MatchImages(folder_path='images', target_path=target_path, threshold=self.threshold)
                res_bool = matcher.match_threshold()
                self.df.iloc[i, 4] = res_bool
            else:
                pass
                #scraper.get_banners(page = "medicamentos")
                #target_path = os.path.join(self.folder_path, self.df.iloc[i, 3])
                #matcher = MatchImages(folder_path='images', target_path=target_path, threshold=self.threshold)
                #res_bool = matcher.match_threshold()
                #self.df.iloc[i, 4] = res_bool
        return self.df
