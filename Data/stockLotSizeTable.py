from ast import ImportFrom
from nsepython import nse_get_fno_lot_sizes
import pandas

def get_all_lot_sizes():
    stocklist = nse_get_fno_lot_sizes(symbol="all", mode="list")
    stockListStockNames = list(stocklist.keys())
    stocklistStockLotSize = list(stocklist.values())
    newDict = {
        "stockName": stockListStockNames,
        "stockListStockLotSize": stocklistStockLotSize
    }
    df = pandas.DataFrame(newDict)
    dfsort =df.sort_values("stockListStockLotSize")
    records = dfsort.to_dict(orient="records")
    return records
