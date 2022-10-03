import yfinance as yf
import datetime
from datetime import date, timedelta

today = date.today()
end_date = today.strftime("%Y/%m/%d")
date_start = today - timedelta(days=360)
start_date = date_start.strftime("%Y/%m/%d")



def getStockHistiory():
    stockHistory = yf.download("^NSEI",
                                start= start_date,
                                end= end_date,
                                interval= '5m',
                               rounding=True)
    return stockHistory