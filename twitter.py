from requests_oauthlib.oauth1_session import OAuth1Session
import tweepy
import config
import json
import os
from dotenv import load_dotenv
load_dotenv()

# トークン等取得
AK = os.environ['TWITTER_DMM_API_KEY']
AS = os.environ['TWITTER_DMM_API_SECRET_KEY']
AT = os.environ['TWITTER_DMM_ACCESS_TOKEN']
ATS = os.environ['TWITTER_DMM_ACCESS_TOKEN_SECRET']
BT = os.environ['TWITTER_DMM_BEARER_TOKEN']


# Twitterオブジェクトの生成
client = tweepy.Client(BT, AK, AS, AT, ATS)

class Twitter:
    def __init__(self, title, price, url):
        self.title = title
        self.price = price
        self.url = url

    ##
    ## DMMの情報をツイートする
    ##
    def tweet_dmm_info(self):
        # ツイート内容
        content = self.get_tweet_content()
        print(content)

        # ツイートを投稿
        res = client.create_tweet(text=content)
        print(res)

    ##
    ## ツイート内容を取得する
    ##
    def get_tweet_content(self):
        content = '【期間限定セール!!】\n'
        content += f'通常価格{self.price}円が超お買い得に!!\n\n'
        content += f'{self.title}\n'
        content += f'{self.url}'

        return content
