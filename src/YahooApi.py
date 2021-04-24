import uno
import unohelper
import requests
import re

from com.stock.api.yahoo import XStockYahoo

class YahooImpl(unohelper.Base, XStockYahoo):

    def __init__(self, ctx):
        self.ctx = ctx

    def YAHOOPRICE(self, symbol):
        yahoo_base_url = "http://finance.yahoo.com/quote/"
        url_to_query = yahoo_base_url + symbol
        try:
            ws = requests.get(url_to_query)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        content = ws.text
        regex = re.compile(r"data-reactid=\"32\">[0-9|\.|\,]+<")
        result = regex.search(content)
        if result:
            content = result.group(0)
            results = re.findall(r"[0-9|\.|\,]+", content);
            return float(results[1])
        else:
            return float(0)
        
    def YAHOOHIGHPRICE(self, symbol):
        yahoo_base_url = "http://finance.yahoo.com/quote/"
        url_to_query = yahoo_base_url + symbol
        try:
            ws = requests.get(url_to_query)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        content = ws.text
        regex = re.compile(r"data-test=\"DAYS_RANGE-value\" data-reactid=\"61\">[0-9|\.|\,]+ - [0-9|\.|\,]+<")
        result = regex.search(content)
        if result:                                    
            regex = re.compile(r"[0-9|\.|\,]+ - [0-9|\.|\,]+")   
            result = regex.search(result.group(0))          
            return float(result.group(0).split('-')[1])                          
        else:
            return float(0) 
        
    def YAHOOLOWPRICE(self, symbol):
        yahoo_base_url = "http://finance.yahoo.com/quote/"
        url_to_query = yahoo_base_url + symbol
        try:
            ws = requests.get(url_to_query)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        content = ws.text
        regex = re.compile(r"data-test=\"DAYS_RANGE-value\" data-reactid=\"61\">[0-9|\.|\,]+ - [0-9|\.|\,]+<")
        result = regex.search(content)
        if result:                                    
            regex = re.compile(r"[0-9|\.|\,]+ - [0-9|\.|\,]+")   
            result = regex.search(result.group(0))          
            return float(result.group(0).split('-')[0])                          
        else:
            return float(0) 
        
    def YAHOOVOLUME(self, symbol):
        yahoo_base_url = "http://finance.yahoo.com/quote/"
        url_to_query = yahoo_base_url + symbol
        try:
            ws = requests.get(url_to_query)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        content = ws.text
        regex = re.compile(r"data-reactid=\"70\">[0-9|\.|\,]+<")
        result = regex.search(content)
        if result:
            content = result.group(0)                                    
            results = re.findall(r"[0-9|\.|\,]+", content);   
            return float(results[1].replace(',', ''))                          
        else:
            return float(0)  

def createInstance(ctx):
    return YahooImpl(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,
    "COM.STOCK.API.YAHOO.PYTHON.YAHOOIMPL",
    ("com.sun.star.sheet.AddIn",)
)
