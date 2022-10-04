from django.db import models

from .currentValue import currentValueOfStock
from .historyData import getStockHistiory


def getCurrentValueOfStock():
    return currentValueOfStock()

def getDataOfStock():
    return getStockHistiory()