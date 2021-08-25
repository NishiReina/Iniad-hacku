from django.shortcuts import render
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
instagramID = "17841449060627485"
ACCESS_TOKEN1 = "EAAa6dAwDe5IBAPaokcLfEmtZBMi6Hlcxufb9gEdsNVZCgbioZB1jKN0uDczPouHxLNZBIlxm46JtZB0WBWipVvc1ldxD5PfySy1MlN1l7FW23613dosprzwaGXxCqJunN9ZCmumuqpkf0O2tEZCptVqPEDecjZAKw6ZB7IP0YLQDCE1BKaezH1zAZARdD7RrpJJycZD"

# Create your views here.
def top(request):
    return render(request, 'TotalWeb/top.html')
def test(request):

    return render(request, 'TotalWeb/test.html', json)




json = {
    "data" : [
    {
        "type" : 1, 
        "id" : 1234567891,
        "user_name" : "koki",
        "media_url": "",
        "content": "夢に鈴木マキアートくんが出てきた疲れた顔♡\n夢で会えてよかった。デュフフ",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 2,
        "id" : 1234567892,
        "user_name" : "koki",
        "media_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.29350-15/239347054_257727499510716_6129467660026443754_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8ae9d6&_nc_ohc=gi0wcnol43UAX-jn55f&_nc_ht=scontent-nrt1-1.cdninstagram.com&edm=AEoDcc0EAAAA&oh=3f40082f06a4dda46d45f7ac203d519f&oe=61256AB0",
        "content": "🥕🍰\n#cafe \n#カフェ \n#キャロットケーキ \n#カフェラテ \n#マキアート \n#カフェ巡り \n#カフェ好きな人と繋がりたい \n#いいね返し \n#フォロー返します \n#fff",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 1,"type" : 1,
        "id" : 1234567893,
        "user_name" : "koki",
        "media_url": "",
        "content": "夢に鈴木マキアートくんが出てきた疲れた顔♡\n夢で会えてよかった。デュフフ",
        "timestamp": "2021-08-21T07:56:39+0000"
    },
    {
        "type" : 1,
        "id" : 1234567894,
        "user_name" : "koki",
        "media_url": "https://pbs.twimg.com/media/E9OTOOiVgAEdEWS?format=jpg&name=large",
        "content": "みんなぁ配信見てくれてありがとう青のハート緑のハート黄色のハート紫のハート❤光るハートきらめくハート\nとってもマキアートな配信だったね(๑•ω-๑)♡\nみんなでわいわい盛り上がれて今日も今日とて大満足だよねって話だよね愛してるのジェスチャー\n次の配信は、明日の夕方16:00からだよん！！よろしくお願いしマキアート･:*+.(( °ω° ))/.:+\nおつはなぁ((ヾ(･д･｡)ﾌﾘﾌﾘ",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 2,
        "id" : 1234567895,
        "user_name" : "koki",
        "media_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.29350-15/239347054_257727499510716_6129467660026443754_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8ae9d6&_nc_ohc=gi0wcnol43UAX-jn55f&_nc_ht=scontent-nrt1-1.cdninstagram.com&edm=AEoDcc0EAAAA&oh=3f40082f06a4dda46d45f7ac203d519f&oe=61256AB0",
        "content": "🥕🍰\n#cafe \n#カフェ \n#キャロットケーキ \n#カフェラテ \n#マキアート \n#カフェ巡り \n#カフェ好きな人と繋がりたい \n#いいね返し \n#フォロー返します \n#fff",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 1,
        "id" : 1234567896,
        "user_name" : "koki",
        "media_url": "",
        "content": "夢に鈴木マキアートくんが出てきた疲れた顔♡\n夢で会えてよかった。デュフフ",
        "timestamp": "2021-08-21T07:56:39+0000"
    },
    {
        "type" : 2,
        "id" : 1234567897,
        "user_name" : "koki",
        "media_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.29350-15/239347054_257727499510716_6129467660026443754_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8ae9d6&_nc_ohc=gi0wcnol43UAX-jn55f&_nc_ht=scontent-nrt1-1.cdninstagram.com&edm=AEoDcc0EAAAA&oh=3f40082f06a4dda46d45f7ac203d519f&oe=61256AB0",
        "content": "🥕🍰\n#cafe \n#カフェ \n#キャロットケーキ \n#カフェラテ \n#マキアート \n#カフェ巡り \n#カフェ好きな人と繋がりたい \n#いいね返し \n#フォロー返します \n#fff",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 2,
        "id" : 1234567898,
        "user_name" : "koki",
        "media_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.29350-15/239347054_257727499510716_6129467660026443754_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8ae9d6&_nc_ohc=gi0wcnol43UAX-jn55f&_nc_ht=scontent-nrt1-1.cdninstagram.com&edm=AEoDcc0EAAAA&oh=3f40082f06a4dda46d45f7ac203d519f&oe=61256AB0",
        "content": "🥕🍰\n#cafe \n#カフェ \n#キャロットケーキ \n#カフェラテ \n#マキアート \n#カフェ巡り \n#カフェ好きな人と繋がりたい \n#いいね返し \n#フォロー返します \n#fff",
        "timestamp": "2021-08-21T07:56:39+0000"
    }, 
    {
        "type" : 2,
        "id" : 1234567899,
        "user_name" : "koki",
        "media_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.29350-15/239347054_257727499510716_6129467660026443754_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=8ae9d6&_nc_ohc=gi0wcnol43UAX-jn55f&_nc_ht=scontent-nrt1-1.cdninstagram.com&edm=AEoDcc0EAAAA&oh=3f40082f06a4dda46d45f7ac203d519f&oe=61256AB0",
        "content": "🥕🍰\n#cafe \n#カフェ \n#キャロットケーキ \n#カフェラテ \n#マキアート \n#カフェ巡り \n#カフェ好きな人と繋がりたい \n#いいね返し \n#フォロー返します \n#fff",
        "timestamp": "2021-08-21T07:56:39+0000"
    },
    {
        "type" : 1,
        "id" : 1234567890,
        "user_name" : "koki",
        "media_url": "https://pbs.twimg.com/media/E9OTOOiVgAEdEWS?format=jpg&name=large",
        "content": "みんなぁ配信見てくれてありがとう青のハート緑のハート黄色のハート紫のハート❤光るハートきらめくハート\nとってもマキアートな配信だったね(๑•ω-๑)♡\nみんなでわいわい盛り上がれて今日も今日とて大満足だよねって話だよね愛してるのジェスチャー\n次の配信は、明日の夕方16:00からだよん！！よろしくお願いしマキアート･:*+.(( °ω° ))/.:+\nおつはなぁ((ヾ(･д･｡)ﾌﾘﾌﾘ",
        "timestamp": "2021-08-21T07:56:39+0000"
    }]}

    

def twitter_get_id(request):
    """ツイッターのid取得"""
    tweet_id_url = [] #ツイートID
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

def twitter_show(tweet_id):
    Twitter = Twython(API_KEY, API_SECRET,ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    tweet = Twitter.show_status(id=tweet_id)
    param = {
    'type' : 1,
    'id' : tweet_id,
    # 'user_name' : tweet['user']['name'],
    # 'media_url' : url,
    'content' : tweet['text'],
    'timestamp': tweet['created_at']
    }
    return param

# def instagram_get_id(request):
#     insta_id_url = [] #投稿ID
#     id_search_url = "https://graph.facebook.com/ig_hashtag_search?user_id=" + instagramID + "&q=" + request +  "&access_token=" + ACCESS_TOKEN1
#     response = requests.get(id_search_url)
#     hash_id = response.json()
#     serch_type = "recent_media"
#     url = "https://graph.facebook.com/v9.0/" + hash_id["data"][0]["id"] + "/" + serch_type + "?user_id=" + instagramID + "&access_token=" + ACCESS_TOKEN + "&fields=id,media_url,caption,timestamp,children{id,media_url}&limit=10"
#     response = requests.get(url)
#     response.json()["data"]
#     item = response.json()["data"]
#     for i in item:
#         print(i["id"])
#         insta_id_url.append(i["id"])
#     return insta_id_url

def insta_show(request): 
    id_search_url = "https://graph.facebook.com/ig_hashtag_search?user_id=" + instagramID + "&q=#" + request +  "&access_token=" + ACCESS_TOKEN1
    response = requests.get(id_search_url)
    hash_id = response.json()
    serch_type = "recent_media"
    url = "https://graph.facebook.com/v9.0/" + hash_id["data"][0]["id"] + "/" + serch_type + "?user_id=" + instagramID + "&access_token=" + ACCESS_TOKEN1 + "&fields=id,media_url,caption,timestamp,children{id,media_url}&limit=2"
    response = requests.get(url)
    insta_dict = {"data":[]}
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
        insta_dict["data"].append(param)
    return insta_dict


        


