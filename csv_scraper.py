import requests
import os

stocks = ['2330', '6183']
for stock in stocks:

    re = requests.get(f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date=20220813&stockNo={stock}')

    if not os.path.exists('csv'):
        os.mkdir('csv')

    with open(f'csv\\{stock}.csv', 'wb') as file:
        file.write(re.content)