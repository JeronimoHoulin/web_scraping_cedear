"""
Created on Sun Jan 24 09:38:53 2021

@author: jeron
"""


############# Beautiful Soup ###############
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url_stock = "https://es.investing.com/equities/apple-computer-inc"

request_stock = Request(url_stock, headers={'User-Agent': 'Mozilla/5.0'})
page_stock = urlopen(request_stock).read()

soup_stock = BeautifulSoup(page_stock, 'html.parser')
#print(soup_stock)

#Inspect the source code and see if its span, dic, table... and copy the class in there...
precio_stock = soup_stock.find('span', {'class':'arial_26 inlineblock pid-6408-last'}).text

#Inspect the source code and see if its span, dic, table... and copy the class in there...
#Queda en STR
precio_stock = soup_stock.find('span', {'class':'arial_26 inlineblock pid-6408-last'}).text


######################################################################################

url_cede = "https://www.invertironline.com/titulo/cotizacion/BCBA/AAPL/APPLE/"

request_cede = Request(url_cede, headers={'User-Agent': 'Mozilla/5.0'})
page_cede = urlopen(request_cede).read()

soup_cede = BeautifulSoup(page_cede, 'html.parser')
#print(soup_cede)

precio_cede = soup_cede.find('span', {'data-field':'UltimoPrecio'}).text



######################################################################################

url_tc = "https://www.dolarhoy.com/cotizacion-dolar-mep"

request_tc = Request(url_tc, headers={'User-Agent': 'Mozilla/5.0'})
page_tc = urlopen(request_tc).read()

soup_tc = BeautifulSoup(page_tc, 'html.parser')
#print(soup_tc)

precio_tc = soup_tc.find('div', {'class':'value'}).findNext('div', {'class':'value'}).contents[0]

#Clean up and turn STR into FLOAT 
#https://www.youtube.com/watch?v=gKHCdYsxRew&ab_channel=DeveloperTharun
import re    #Function for clean up

precio_stock = float(re.sub(r'[\D]' , '' , precio_stock))  /100 #\D removes all non digit signs in the str
precio_cede =  float(re.sub(r'[\D]' , '' , precio_cede))  /100   #y dividido 100 para que encuadren los decimales
precio_tc = float(re.sub(r'[\D]' , '' , precio_tc)) /100




############## Pandas ####################
import pandas as pd

#pandas has a function named read html
df_cede = pd.read_html('https://www.rava.com/precios/panel.php?m=CED')
df_cede = df_cede[8] # esto es por que toma todas las tablas, y si hay varias acá le decís cual querés.
df_cede = df_cede.drop(["1", "2", "3", "4","5", "6"], axis=0)

# esto solo busca TABLAS.. así que no es muy útil para buscar un solo precio que en gnral aparece solo en las paginas. 



############## YFinance / yahoo_finance ################
import yfinance as yf

aapl_eeuu = yf.Ticker("AAPL")

from yahoo_fin import stock_info as si

aapl_eeuu = si.get_live_price("aapl")          #yahoo_finance saca el ult precio en vivo.. yfinance el historial.
aapl_arg = si.get_live_price("aapl.ba")








################ Estrategia con Cedears ####################
#Variables:
precio_stock = precio_stock
precio_cede = precio_cede
tipo_cambio = precio_tc
ratio = 10 # Establecido por el Banco Comafi

#Estrategia:
def cedear_strat_101(stock, cedear, tc, ratio):
    if cedear / tc * ratio > stock:
        print("El Cedear está Caro ! \n" + "Precio del Cedear: $" + str(round(cedear/tc*ratio,2)) +"\nPrecio de la Acción: $" + str(stock))
    elif cedear / tc * ratio < stock:
        print("El Cedear está Barato ! \n" + "Precio del Cedear: $" + str(round(cedear/tc*ratio,2)) +"\nPrecio de la Acción: $" + str(stock))
    else:
        print("Mercado se encuentra en equilibrio.")


cedear_strat_101(precio_stock, precio_cede, tipo_cambio, 10)














