from django.shortcuts import render

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