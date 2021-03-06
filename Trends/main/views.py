from django.shortcuts import render
from pytrends.request import TrendReq
import pandas as pd
import json

# 한 사용자는 4시간 동안 1,400건의 순차적 요청이 한계에 도달했다고 보고했지만
# 이는 쿼리 크기와 요청 빈도에 따라 다를 수 있다.
# pytrends의 api 동접 얼마인지 확인해야할듯


def index(request):
    return render(request, 'index.html', top(request))

# def getYotubeResult(request):

#     videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)
#     print(videosSearch.result())


def getTrend(country):
    country_abbrev = {'kr': 'south_korea', 'jp': 'japan',
                      'us': 'united_states','uk': 'united_kingdom',
                      'krtest': 'south_korea','jptest':'japan','ustest':'united_states',
                      'uktest':'united_kingdom'}

    pytrend = TrendReq()
    trends_kr = pytrend.trending_searches(
        pn=country_abbrev[country])  # trends_kr에 S.Korea 트렌드 순위 저장

    file = 'Trends_' + country + '.csv'

    # trends_kr 변수에 들어있는 정보를 csv 파일로 저장
    trends_kr.to_csv(file, encoding='utf-8-sig')
    # .csv 파일 여기로 불러오기 (df = DataFrame)
    df = pd.read_csv(file)

    # df의 타입을 pandas.dataframe -> 로 변경!
    json_records = df.reset_index().to_json(orient='records')
    jsonData = []
    jsonData = json.loads(json_records)


    # topic은 구글 트렌드 제목임. 제목들을 합쳐서 list로 변경
    topics = df['0'].tolist()


    videoURLs = []
    for topic in topics:
        topic = topic.replace(' ', '+')
        videoURLs.append(
            'https://www.youtube.com/results?search_query=' + topic)

    naverURLs = []
    for topic in topics:
        topic = topic.replace(' ', '+')
        naverURLs.append(
            'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + topic)

    googleURLs=[]
    for topic in topics:
        topic = topic.replace(' ','+')
        googleURLs.append(
            'https://www.google.com/search?q='+topic+'&newwindow=1&sxsrf=ALeKk01fTIbPHY0S5JArWZwx982u9Rc-iA:1622361169905&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjF0eqp9vDwAhUKCqYKHTHmAJ8Q_AUoAXoECAEQAw&biw=1536&bih=722'
        )

    if country=='krtest' or country=='uktest' or country=='ustest' or country=='jptest':
        data=topics[0]
    else:
        data = []
        for i in range(0, 20):  
            data.append({'index': i+1, 'd': jsonData[i], 'videoURL': videoURLs[i], 'naverURL': naverURLs[i], 'googleURL':googleURLs[i]})

    # print(data)
    
    return {'data': data}



def top(request):
    topOnes = [getTrend('krtest'), getTrend('ustest'), getTrend('jptest'), getTrend('uktest')]

    krtop=topOnes[0]['data']
    ustop=topOnes[1]['data']
    jptop=topOnes[2]['data']
    uktop=topOnes[3]['data']
    
    return{'krtop':krtop,'ustop':ustop,'jptop':jptop,'uktop':uktop}   


def trend_all(request, country):
    context = getTrend(country)
    return render(request, 'trend_' + country + '.html', context)
