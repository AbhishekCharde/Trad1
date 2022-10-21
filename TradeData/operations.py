import tradeData.models as models
import json

def get_stock_symbol_list():
    stock_list = models.getStockList()
    return json.dumps(stock_list)