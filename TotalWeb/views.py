from django.shortcuts import render
import logging
import tweepy
import json
import datetime
import requests
from twython import Twython

# APIkey
API_KEY = 'nzz81gXwZfMbvOoBfFfGlQC4s'
API_SECRET = '3BUjtqoz0HwAiLfGnEKJ8YoxoHYg6BVXJqpkPEGzg2xLum2QrM'
ACCESS_TOKEN = '1420094993084026881-Ljl1gCaFkYUz4dXp2z2nQbIKaFCbiA'
ACCESS_TOKEN_SECRET = 'Vtwk9CKX5KIi43sp8aSXy5mt6isrb0LPndHfQGSz8rxmG'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#insta API key
# instagramID = "17841449060627485"
instagramID = "108260311518775"
ACCESS_TOKEN1='EAAa6dAwDe5IBAL0ZAjLnF9fqMFTI7sOWe0jK6WOd6FpxIjytr6ftmBKNEMkY8kj2nyy3OrxU6d9GJBUM6sDe5N1nJyqBayPjQ4yFpqLHKUyQH2w6Nt7EiQabKjaaVxx3PxJa6d7eFpnd1TDZAOUwuuhTrx1jbi63xnWsspU2T8HcS7MxugEpoM16ceXV2gDyOko8BfoAZDZD'

# Create your views here.
def top(request):
    return render(request, 'TotalWeb/top.html')


def search(request):
    search = request.POST.get("search")
    data={ "data" : []}
    id_lst, img_dict = twitter_get_id("#" + search)
    # insta_lst = insta_show("#" + search)
    for i in id_lst:
        params = twitter_show(i)
        params["type"] = 1
        if (i in img_dict):
            params["media_url"] = img_dict[i]
        else:
            params["media_url"] = ""
        data["data"].append(params)
    # data["data"] = data["data"] + insta_lst

    return render(request, 'TotalWeb/test.html', data)
    

def twitter_get_id(request):
    """ツイッターのid取得"""
    tweet_id_url = [] #ツイートID
    tweet_dict = {}    #画像があるツイートIDと画像urlを格納

    # 最近のツイート情報10件取得
    tweets = api.search(q=[request], result_type="recent", count=20)
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


def twitter_show(tweet_id):
    Twitter = Twython(API_KEY, API_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    tweet = Twitter.show_status(id=tweet_id)

    param = {
        'type' : 1,
        'id' : tweet_id,
        'user_name' : tweet['user']['name'],
        # 'media_url' : url,
        'content' : tweet['text'],
        'timestamp': tweet['created_at']
    }

    return param


def insta_show(request): 
    id_search_url = "https://graph.facebook.com/v11.0/ig_hashtag_search?user_id=106314948445094&q=リベンジャーズ&access_token=EAAHpCT8uFBsBAESecayp1afEl1uZBv8Vtpxn8Tsy7YgEl2hXVZCTfVfId8zrc1WNrTKRdOhLrgUFGm9phFPDuqkbF99mAZCwbiFTP4jfdnyytxMViJXeafTQeW3eg1cZBQJ3bBOWKWyXM49d5CzwOVZA0Ch2Sg4RCYRHz8HqFij9ZCiVcvLTE6"
    response = requests.get(id_search_url)
    hash_id = response.json()
    serch_type = "recent_media"
    url = "https://graph.facebook.com/v11.0/" + hash_id["data"][0]["id"] + "/" + serch_type + "?user_id=" + instagramID + "&access_token=" + ACCESS_TOKEN1 + "&fields=id,media_url,caption,timestamp,children{id,media_url}&limit=10"
    response = requests.get(url)
    insta_lst = []
    for i in response.json()["data"]:
            param = {
                'type': 2,
                'id' : i["id"],
                'content' : i["caption"],
                'timestamp' : i["timestamp"],
            }
            if "children" in i:
                for t in i["children"]["data"]:
                    param["media_url"] = t["media_url"]
                    break
            else:
                param["media_url"] = i["media_url"]
            insta_lst.append(param)
    return insta_lst

