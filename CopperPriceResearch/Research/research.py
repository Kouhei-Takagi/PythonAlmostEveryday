import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Research:
    def __init__(self, data):
        self.data = data

    def calculate_log(self):
        self.data['log'] = np.log(self.data['Close'])
        return self.data
    
    def plot_data(self, forecast=None):
        plt.figure(figsize=(12,6))
        plt.plot(self.data.index, self.data['log'], label='Original')
        if forecast is not None:
            last_date = self.data.index[-1]
            prediction_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=len(forecast))
            plt.plot(prediction_dates, forecast, label='Forecasted')
        plt.title('Logarithmic Value of Close Price over Time')
        plt.xlabel('Date')
        plt.ylabel('Logarithmic Value')
        plt.legend()
        plt.grid(True)
        plt.show()
        