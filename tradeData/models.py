from django.db import models

from TradeData.currentValue import currentValueOfStock
from TradeData.historyData import getStockHistiory


def getCurrentValueOfStock():
    return currentValueOfStock()

def getDataOfStock():
    return getStockHistiory()