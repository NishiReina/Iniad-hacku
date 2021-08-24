from django.shortcuts import render
import tweepy
import json
import datetime
from twython import Twython

# APIkey
API_KEY = 'nzz81gXwZfMbvOoBfFfGlQC4s'
API_SECRET = '3BUjtqoz0HwAiLfGnEKJ8YoxoHYg6BVXJqpkPEGzg2xLum2QrM'
ACCESS_TOKEN = '1420094993084026881-Ljl1gCaFkYUz4dXp2z2nQbIKaFCbiA'
ACCESS_TOKEN_SECRET = 'Vtwk9CKX5KIi43sp8aSXy5mt6isrb0LPndHfQGSz8rxmG'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Create your views here.
def top(request):
    return render(request, 'TotalWeb/top.html')
def test(request):
    return render(request, 'TotalWeb/test.html')

def twitter_get_id(request):
    """ツイッターのid取得"""
    tweet_id_url = []　#ツイートID
    tweet_dict = {}    #画像があるツイートIDと画像urlを格納

    # 最近のツイート情報10件取得
    tweets = api.search(q=[request], result_type="recent", count=10)
    for tweet in tweets:
        try:
            # 画像url取得
            url = tweet.extended_entities['media'][0]['media_url']
        except:
            # 画像がなかった場合
            url = False
        else:
            # 画像があった場合tweet_dictに追加
            tweet_dict[tweet.id] = url
        finally:
            # 10件のIDを格納
            tweet_id_url.append(tweet.id)
    return tweet_id_url, tweet_dict

    def twitter_save_id(tweet_id):
    """idからツイッターの情報取得"""
    Twitter = Twython(API_KEY, API_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    tweet = Twitter.show_status(id=tweet_id)
        param = {
        'id' : tweet_id,
        # 'user_name' : tweet['user']['name'],
        # 'media_url' : url,
        'content' : tweet['text'],
        'timestamp': tweet['created_at']
        }
    return param
