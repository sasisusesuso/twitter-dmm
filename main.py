import scraping as sp
import twitter as tw
import line as ln

def main():
    try:
        # DMMの情報を取得
        scraping = sp.Scraping()
        scraping.get_dmm_info()
        title, price, url = scraping.get_dmm_info()

        # DMMの情報をツイートする
        twitter = tw.Twitter(title, price, url)
        twitter.tweet_dmm_info() 

    except Exception    as e:
        print(e)
        
        # エラー内容LINE通知
        # line = ln.Line()
        # line.send_message(e)

if __name__ == '__main__':
    main()
