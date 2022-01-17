import requests
from config import AV_API_KEY

class EndOfDayAPI:

    def get(self, stock_ticker):
        params = {
            'apikey': AV_API_KEY
        }
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}'.format(stock_ticker)
        response = requests.get(url, params=params)
        print(response.json())
        return response.json()

