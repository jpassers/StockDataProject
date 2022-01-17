from models import *


class CreateRecord:
    def stock_eod_price(self, stock_ticker, eod_date, open_price, eod_price):
        StockEODPrice.create(
            stock_ticker=stock_ticker,
            eod_date=eod_date,
            open_price=open_price,
            eod_price=eod_price,
        )


class UpdateRecord:
    def stock_eod_price(self):
        pass


class DeleteRecord:
    def stock_eod_price(self):
        pass


class ReadRecord:
    def stock_eod_price(self):
        pass
