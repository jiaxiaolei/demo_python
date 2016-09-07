#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此输入您的Key
#ACCESS_KEY=""
#SECRET_KEY=""

#ACCESS_KEY="a7b18bd1-d58459b8-d1faba30-1519b"
#SECRET_KEY="6641d003-a7e72e01-c91c8711-3c7ba"

ACCESS_KEY="e3977f44-8f677210-00116494-af291"
SECRET_KEY="7f57a383-1f3a8d46-343e394a-8621a"

HUOBI_SERVICE_API="https://api.huobi.com/apiv3"

BUY = "buy"
BUY_MARKET = "buy_market"
CANCEL_ORDER = "cancel_order"
ACCOUNT_INFO = "get_account_info"
NEW_DEAL_ORDERS = "get_new_deal_orders"
ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"
GET_ORDERS = "get_orders"
ORDER_INFO = "order_info"
SELL = "sell"
SELL_MARKET = "sell_market"

def signature(params):
    params = sorted(params.items(), key=lambda d:d[0], reverse=False)
    #params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    #message = urllib.urlencode(params)
    message = urllib.parse.urlencode(params)
    m = hashlib.md5()
    #m.update(message)
    m.update(message.encode("utf8")) # py3
    m.digest()
    sig=m.hexdigest()
    return sig

