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

# AK = os.environ.get('TWITTER_DOT_API_KEY')
# AS = os.environ.get('TWITTER_DOT_API_SECRET_KEY')
# AT = os.environ.get('TWITTER_DOT_ACCESS_TOKEN')
# ATS = os.environ.get('TWITTER_DOT_ACCESS_TOKEN_SECRET')
# BT = os.environ.get('TWITTER_DOT_BEARER_TOKEN')
AK = config.TWITTER_DMM_API_KEY
AS = config.TWITTER_DMM_API_SECRET_KEY
AT = config.TWITTER_DMM_ACCESS_TOKEN
ATS = config.TWITTER_DMM_ACCESS_TOKEN_SECRET
BT = config.TWITTER_DMM_BEARER_TOKEN


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
        api = dmm.API(api_id=config.API_ID, affiliate_id=config.AFFILIATE_ID)

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