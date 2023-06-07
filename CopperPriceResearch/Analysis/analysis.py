from statsmodels.tsa.arima.model import ARIMA

class Analysis:
    def __init__(self, data):
        self.data = data

    def predict(self, steps=10):
        model = ARIMA(self.data['log'], order=(5,1,0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
        return forecast.values
