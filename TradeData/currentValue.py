import yahoo_fin.stock_info as si


def currentValueOfStock():
    current_val = si.get_live_price("^NSEI")
    current_val = "{:.2f}".format(current_val)
    return current_val