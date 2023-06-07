import yfinance as yf
import pandas as pd

class Data:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
    
    def get_data(self):
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return data