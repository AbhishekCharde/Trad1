from django.shortcuts import render,HttpResponse
from django.template import loader
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import tradeData.models as models



def index(request):
    stockLive = models.getCurrentValueOfStock()
    
    context = {"stockprice": stockLive}
    return render(request, 'index.htm',context=context)

def portfolio(request):
    context = {'segment': 'portfolio'}

    html_template = loader.get_template('portfolio.html')
    return HttpResponse(html_template.render(context, request))
    # return HttpResponse('')
    # return render(request,'portfolio.html')

def profile(request):
    return render(request,'profile.html')

def stockdata(request):
    return render(request,'stockdata.html',)

def telegramchannels(request):
    return render(request,'telegramchannels.html')

def contactus(request):
    return render(request,'contactus.htm')

def stockdetails(request):
    return render(request, 'stockDetails.htm')