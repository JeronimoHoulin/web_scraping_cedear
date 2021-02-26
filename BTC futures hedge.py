"""
Created on Sun Jan 24 09:38:53 2021

@author: jeron
"""



############# Beautiful Soup ###############
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re    #Function for clean up



#BTC SPOT

btc_url  = "https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch"

request_btc = Request(btc_url, headers={'User-Agent': 'Mozilla/5.0'})
page_btc = urlopen(request_btc).read()

soup_btc = BeautifulSoup(page_btc, 'html.parser')
#print(soup_stock)

#Inspect the source code and see if its span, dic, table... and copy the class in there...
price_btc = soup_btc.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

#Still in STR format

price_btc = float(re.sub(r'[\D]' , '' , price_btc))  /100  
#\D removes all non digit signs in the str  divide by 100 so decimals line up.


#BTC FUTURES monthly

btcf_url  = "https://finance.yahoo.com/quote/BTM%3DF/futures?p=BTM%3DF"

request_btcf = Request(btcf_url, headers={'User-Agent': 'Mozilla/5.0'})
page_btcf = urlopen(request_btcf).read()

soup_btcf = BeautifulSoup(page_btcf, 'html.parser')
#print(soup_stock)

#Inspect the source code and see if its span, dic, table... and copy the class in there...
price_btcf = soup_btcf.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

#Still in STR format

price_btcf = float(re.sub(r'[\D]' , '' , price_btcf))  /100  
#\D removes all non digit signs in the str  divide by 100 so decimals line up.


#Hedge Package 
amount_btc = 10
def package_hedge(price_btcf, price_btc, amount_btc):
    prcnt = (price_btcf - price_btc)/price_btcf
    if price_btc < price_btcf:
        print("You will have to earn at least {}%, in one month´s time, to make a profit. You´re in CONTANGO.".format(round(prcnt*100, 3)))
    if price_btc > price_btcf:
        print("You can loose up to {}%, in one month´s time, and still make a profit. You´re in BACKWARDATION.".format(round(-prcnt*100, 3)))



package_hedge(price_btcf, price_btc, amount_btc)