from db import CreateRecord
from request import EndOfDayAPI

if __name__ == "__main__":
    ticker_list = ['BP', 'BA']

    for ticker in ticker_list:
        eod_data = EndOfDayAPI().get(ticker)
        refreshed_date = eod_data['Meta Data']['3. Last Refreshed']

        for item in eod_data['Time Series (Daily)']:
            CreateRecord().stock_eod_price(
                eod_date=item,
                stock_ticker=eod_data['Meta Data']['2. Symbol'],
                open_price=eod_data['Time Series (Daily)'][refreshed_date]['1. open'],
                eod_price=eod_data['Time Series (Daily)'][refreshed_date]['4. close']
            )






