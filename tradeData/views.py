import json
from operator import mod
from django.shortcuts import render,HttpResponse
from django.template import loader
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import tradeData.models as models
import tradeData.operations as operations
from json import dumps
 

import Data.getOIData as oi
list_stocks = operations.get_stock_symbol_list()

def base(request):
    # models.getOIData()
    
    return render(request, 'base.htm', {'stockList': list_stocks}) 

def index(request):
    stockLive = models.getCurrentValueOfStock()
    history = models.getHistoryOfStock()
    context = {"stockprice": stockLive,'stockList':list_stocks}
    
    return render(request, 'index.htm',context=context)

def portfolio(request):
    context = {'segment': 'portfolio','stockList':list_stocks}
    # oi.get_oi_data()
    html_template = loader.get_template('portfolio.html')
    return HttpResponse(html_template.render(context, request))
    # return HttpResponse('')
    # return render(request,'portfolio.html')

def profile(request):
    return render(request,'profile.html',{'stockList':list_stocks})

def stockdata(request):
    return render(request,'stockdata.html',{'stockList':list_stocks})

def telegramchannels(request):
    return render(request,'telegramchannels.html',{'stockList':list_stocks})

def contactus(request):
    return render(request,'contactus.htm',{'stockList':list_stocks})

def stockdetails(request):
    if request.method != 'POST':
        return render(request,'stockDetails.html',{'stockList':list_stocks})
    searched = request.POST['searched']
    stock = models.getStockList()
    oi_data = models.getOIData()
    oi_json = json.dumps(oi_data)
    print(type(oi_data))
    return render(request, 'stockDetails.htm',{'stockName':searched,'stockList':stock,'oiData':oi_json})