from django.shortcuts import render
from pytrends.request import TrendReq
import pandas as pd
import json

def index(request):
    return render(request, 'index.html')

def trend_sa(request):
    pytrend = TrendReq()
    trend_sa = pytrend.trending_searches(pn='south_africa')

    trend_sa.to_csv('Trends_SA.csv', encoding='utf-8-sig')
    df = pd.read_csv("Trends_SA.csv")

    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'trend_sa.html', context)