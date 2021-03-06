# -*- coding: utf-8 -*-
"""Supermercado-Stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nRI_usG4nWH4Hyr9vXAHGfVAFV2K085T

SUPERMERCADO STOCK
"""

#Importar las librerias
import pandas as pd
from bs4 import BeautifulSoup
import requests

#Definir número de paginas
no_pages = 4

#Funcion para obtener los datos de las páginas
def get_data(pageNo):
    headers = {
    'authority': 'www.stock.com.py',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    stock = requests.get('https://www.stock.com.py/search.aspx?searchterms=cafe&pageindex='+str(pageNo), headers=headers)
    content = stock.content
    soup = BeautifulSoup(content)
    alls = []

    #Identificar y recorrer las clases de producto y precio
    for d in soup.findAll('div', attrs={'class':'col-lg-2 col-md-3 col-sm-4 col-xs-6 producto'}):
        #print(d)
        name = d.find('a', attrs={'class':'product-title-link'})
        #print(n[0]['alt'])
        price = d.find('span', attrs={'class':'price-label'})

        all1=[]

        if name is not None:
            #print(n[0]['alt'])
            all1.append(name.text)
        else:
            all1.append('0')  

        if price is not None:
            #print(price.text)
            all1.append(price.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls

#Listar y ordenar los datos en un df
#Agregar columnas necesarias
#Descargar el archivo en formato .csv
results = []
for i in range(1, no_pages+1):
    results.append(get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Name', 'Price'])
df.to_csv('stock_products.csv', index=False, encoding='utf-8')

#Realizar la impresion de los datos obtenidos
df

"""

```
# Este código esta basado en el código de Alejandra Chavez, Msc.
```

"""