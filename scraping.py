from time import time
from bs4 import BeautifulSoup
import requests
import config
import datetime
import tweepy
from requests_oauthlib.oauth1_session import OAuth1Session


from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json
import os
from dotenv import load_dotenv
load_dotenv()

# 追加
import dmm 

API_ID = os.environ['API_ID']
AFFILIATE_ID = os.environ['AFFILIATE_ID']


class Scraping:

    ##
    ## DMMAPIよりスクレイピングして情報取得
    ##
    def get_dmm_info(self):
        # 初期化
        title = ''
        url = ''
        price = ''

        # インスタンスを作成
        api = dmm.API(api_id=API_ID, affiliate_id=AFFILIATE_ID)

        # DMMAPI叩く
        res = api.item_search(site="FANZA", hits=3, keyword=config.KEYWORD, sort=config.SORT)
        res = str(res).replace("'", '"')
        data = json.loads(res)
        title = data["result"]["items"][0]["title"]
        price = data["result"]["items"][0]["prices"]["price"]
        url = data["result"]["items"][0]["affiliateURL"]

        # タイトル修正
        if len(title) >= 100:
            title = title[:99]
        
        # 値段修正
        idx = price.find('~')
        price = price[:idx] 
                
        return title, price, url
