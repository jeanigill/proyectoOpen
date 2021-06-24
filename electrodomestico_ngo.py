# -*- coding: utf-8 -*-
"""Electrodomestico-NGO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfAcOQeOkWMz0ztk1o2z4g8Awin6w2iJ

NGO SAECA - ELECTRODOMESTICOS
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
    'authority': 'ngosaeca.com.py',
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
    stock = requests.get('https://ngosaeca.com.py/buscar/cocina%20a%20gas'+str(pageNo), headers=headers)
    content = stock.content
    soup = BeautifulSoup(content)
    alls = []

    #Identificar y recorrer las clases de producto y precio
    for d in soup.findAll('li', attrs={'class':'product'}):
        #print(d)
        name = d.find('h3', attrs={'class':'menu-item-first-letter-uppercase'})
        #print(n[0]['alt'])
        price = d.find('span', attrs={'class':'amount'})

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
df.to_csv('bristol_products.csv', index=False, encoding='utf-8')

#Realizar la impresion de los datos obtenidos
df

"""

```
# Este código esta basado en el codigo de Alejandra Chaves, Msc.
```

"""