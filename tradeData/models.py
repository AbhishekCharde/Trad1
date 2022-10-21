from django.db import models
import json
from Data.currentValue import currentValueOfStock
from Data.historyData import getStockHistiory
from Data.getOIData import  get_symbol_list, get_oi_scapper


def getCurrentValueOfStock():
    return currentValueOfStock()

def getHistoryOfStock():
    return getStockHistiory()

def getOIData():
    return get_oi_scapper()

def getStockList():
    return get_symbol_list()

