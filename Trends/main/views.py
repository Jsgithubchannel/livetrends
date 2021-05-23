from django.shortcuts import render
from pytrends.request import TrendReq
import pandas as pd
import json

def index(request):
    return render(request, 'index.html')

def trend_kr(request):
    pytrend = TrendReq()
    trend_kr = pytrend.trending_searches(pn='south_korea')

    trend_kr.to_csv('Trends_kr.csv', encoding='utf-8-sig')
    df = pd.read_csv("Trends_kr.csv")

    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'trend_kr.html', context)