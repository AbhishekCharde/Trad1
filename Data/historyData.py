import yfinance as yf
import datetime
from datetime import date, timedelta


today = date.today()
end_date = today.strftime("%Y-%m-%d")
date_start = today - timedelta(days=60)
start_date = date_start.strftime("%Y-%m-%d")



def getStockHistiory():
    print(end_date)
    print(start_date)
    stockHistory = yf.download("^NSEI",
    period='60d',
                                
                                interval= '15m',
                               rounding=True)
    print(stockHistory)
    return stockHistory
