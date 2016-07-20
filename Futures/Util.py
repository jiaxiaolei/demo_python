#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此添加您的key
# ACCESS_KEY=""
# SECRET_KEY=""

ACCESS_KEY="a7b18bd1-d58459b8-d1faba30-1519b"
SECRET_KEY="6641d003-a7e72e01-c91c8711-3c7ba"

def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig
