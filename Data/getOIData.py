# sourcery skip: dict-literal
from sys import displayhook
import Data.NseUrls as NseUrls
import requests
import pandas
import json 
import math
from nsepython import *

symbol_list = ['BAJAJ-AUTO', 'METROPOLIS', 'GAIL', 'HDFC', 'BRITANNIA', 'BEL', 'MANAPPURAM', 'HAVELLS', 'ZYDUSLIFE', 'SBIN', 'AUBANK', 'EICHERMOT', 'PIDILITIND', 'VOLTAS', 'MFSL', 'LALPATHLAB', 'ASHOKLEY', 'JKCEMENT', 'ONGC', 'INDIGO', 'HONAUT', 'INFY', 'HDFCBANK', 'HAL', 'HINDPETRO', 'POWERGRID', 'BHARATFORG', 'PAGEIND', 'GSPL', 'IDFCFIRSTB', 'UBL', 'DEEPAKNTR', 'HINDALCO', 'CIPLA', 'GNFC', 'INDUSINDBK', 'TATACONSUM', 'CANFINHOME', 'GUJGASLTD', 'FSL', 'SBICARD', 'SBILIFE', 'LTTS', 'TORNTPHARM', 'SUNTV', 'ABBOTINDIA', 'UPL', 'TATAPOWER', 'MUTHOOTFIN', 'CHAMBLFERT', 'ASIANPAINT', 'ADANIENT', 'JUBLFOOD', 'TATAMOTORS', 'JSWSTEEL', 'MINDTREE', 'BERGEPAINT', 'GMRINFRA', 'CROMPTON', 'NESTLEIND', 'MRF', 'RECLTD', 'FINNIFTY', 'DRREDDY', 'GRANULES', 'ADANIPORTS', 'OBEROIRLTY', 'BANKNIFTY', 'LICHSGFIN', 'TRENT', 'MCX', 'DALBHARAT', 'HINDUNILVR', 'MARICO', 'NMDC', 'M&M', 'FEDERALBNK', 'NAVINFLUOR', 'ABB', 'MOTHERSON', 'IDFC', 'IEX', 'NATIONALUM', 'INDHOTEL', 'DLF', 'EXIDEIND', 'MARUTI', 'WIPRO', 'TATACHEM', 'ACC', 'AMARAJABAT', 'INDUSTOWER', 'SIEMENS', 'TORNTPOWER', 'CUB', 'SHREECEM', 'COROMANDEL', 'PEL', 'BPCL', 'ATUL', 'AARTIIND', 'BANDHANBNK', 'ZEEL', 'CUMMINSIND', 'LAURUSLABS', 'ULTRACEMCO', 'PVR', 'RAIN', 'HEROMOTOCO', 'ICICIGI', 'ITC', 'ABCAPITAL', 'BIOCON', 'TVSMOTOR', 'SRTRANSFIN', 'MCDOWELL-N', 'LT', 'TECHM', 'BOSCHLTD', 'ASTRAL', 'AXISBANK', 'BALRAMCHIN', 'RELIANCE', 'JINDALSTEL', 'HINDCOPPER', 'IPCALAB', 'MPHASIS', 'BAJAJFINSV', 'HDFCAMC', 'IBULHSGFIN', 'GODREJCP', 'DIVISLAB', 'NIFTY', 'IGL', 'AUROPHARMA', 'LTI', 'PETRONET', 'PNB', 'SYNGENE', 'BALKRISIND', 'DABUR', 'BATAINDIA', 'IDEA', 'MIDCPNIFTY', 'IRCTC', 'CANBK', 'SUNPHARMA', 'APOLLOHOSP', 'GRASIM', 'TITAN', 'ICICIPRULI', 'CONCOR', 'KOTAKBANK', 'INDIACEM', 'COLPAL', 'RBLBANK', 'WHIRLPOOL', 'ABFRL', 'NAUKRI', 'NTPC', 'BSOFT', 'BANKBARODA', 'M&MFIN', 'TATACOMM', 'SAIL', 'CHOLAFIN', 'BHARTIARTL', 'HCLTECH', 'SRF', 'BHEL', 'PFC', 'DELTACORP', 'POLYCAB', 'APOLLOTYRE', 'HDFCLIFE', 'LUPIN', 'COFORGE', 'INTELLECT', 'BAJFINANCE', 'INDIAMART', 'VEDL', 'TCS', 'ALKEM', 'GLENMARK', 'GODREJPROP', 'PERSISTENT', 'COALINDIA', 'AMBUJACEM', 'IOC', 'L&TFH', 'RAMCOCEM', 'MGL', 'ICICIBANK', 'PIIND', 'ESCORTS', 'OFSS', 'DIXON', 'TATASTEEL']
# sess = requests.Session()
# cookies = dict()

def round_nearest(x,num=50): return int(math.ceil(float(x)/num)*num)
def nearest_strike_bnf(x): return round_nearest(x,100)
def nearest_strike_nf(x): return round_nearest(x,50)

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#             'accept-language': 'en,gu;q=0.9,hi;q=0.8',
#             'accept-encoding': 'gzip, deflate, br'}


# def set_cookie():
#     request = sess.get(NseUrls.url_oc, headers=headers, timeout=5)
#     cookies = dict(request.cookies)

# def get_data(url):
#     set_cookie()
#     response = sess.get(url, headers=headers, timeout=5, cookies=cookies)
#     if(response.status_code==401):
#         set_cookie()
#         response = sess.get(url_nf, headers=headers, timeout=5, cookies=cookies)
#     return response.text if (response.status_code==200) else ""

# def set_header():
#     global bnf_ul
#     global nf_ul
#     global bnf_nearest
#     global nf_nearest
#     response_text = get_data(NseUrls.url_oc)
    
#     data = json.loads(response_text)
#     # print(data)
#     for index in data["data"]:
#         if index["index"]=="NIFTY 50":
#             nf_ul = index["last"]
#             # print("nifty")
#         if index["index"]=="NIFTY BANK":
#             bnf_ul = index["last"]
#             print("banknifty")
#     bnf_nearest=nearest_strike_bnf(bnf_ul)
#     nf_nearest=nearest_strike_nf(nf_ul)

# def get_oi_data():
#     print("get_oi_data() returning_params")
#     angle_one_url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
#     df = pandas.read_json(angle_one_url)
#     symbol = [df['name'][i] for i in df.index if df['exch_seg'][i] == 'NFO']
#     # for stock in symbol:

#     symbol = [*set(symbol)]
#     symbol_list.clear()
#     for sym in symbol:
#         symbol_list.append(sym)

#     print(symbol_list)
   
# def print_oi(num,step,nearest,url):
#     strike = nearest - (step*num)
#     start_strike = nearest - (step*num)
#     response_text = get_data(url)
#     data = json.loads(response_text)
#     currExpiryDate = data["records"]["expiryDates"][0]
#     # print(type(data))
#     # if item["expiryDate"] == currExpiryDate:
#     #     df = pandas.read_json(data)
#     a = []
#     for item in data['records']['data']:
#         if item["expiryDate"] == currExpiryDate:
#             # print(item)
#             a.append(item)
#                             # df = pandas.DataFrame.from_dict(data)
#                             # print(df)
#     # print(a)
#     df = pandas.DataFrame.from_records(a)
#     print("Headers:",df.columns)
#     #         print(item)
#     #     # if item["expiryDate"] == currExpiryDate and item["strikePrice"] == strike and item["strikePrice"] < start_strike + (step * num * 2):
#         #     #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
#         #     print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + str(item["CE"]["openInterest"]).rjust(10," ") + " ]" + " PE " + "[ " + str(item["PE"]["openInterest"]).rjust(10," ") + " ]")
#         #     strike = strike + step

def running_status():
    start_now=datetime.datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
    end_now=datetime.datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)
    return start_now<datetime.datetime.now()<end_now

def get():
    print("------------------------------------------------------")
    # print(indices)
    # print("------------------------------------------------------")
    # print(fnolist())
    # print("------------------------------------------------------")
    # print(running_status())
    # print("------------------------------------------------------")
    # print(type(nse_optionchain_scrapper('NIFTY ')))
    # print("------------------------------------------------------")
    # oi_data = oi_chain_builder("RELIANCE","latest","full")
    # print(oi_data)
    # print("------------------------------------------------------")
    # # print(pandas.DataFrame.from_dict(nse_eq("JUSTDIAL")))
    # print(pandas.DataFrame.from_dict(nse_eq("JUSTDIAL")).columns)
    # print("------------------------------------------------------")
    # print(nse_fno("BANKNIFTY"))
    # print("------------------------------------------------------")

def get_symbol_list():
    # set_header()
    # print_oi(10,50,nf_nearest,NseUrls.url_nf)
    get()
    # get_oi_scapper()
    # print(pandas.DataFrame.from_dict(get_oi_scapper()))
    return symbol_list

def get_fno_list():
    return fnolist()

def get_oi_scapper():  
    data = nse_optionchain_scrapper('NIFTY')
    currExpiryDate = data["records"]["expiryDates"][0]
    list = [item for item in data['records']['data'] if item["expiryDate"] == currExpiryDate]

    # print(nse_optionchain_scrapper('NIFTY'))
    return list

