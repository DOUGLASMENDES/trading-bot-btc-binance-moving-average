import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(period=14)

    def next(self):
        if self.data.close[0] > self.sma[0]:
            self.buy()
        elif self.data.close[0] < self.sma[0]:
            self.sell()

# Load history data
data = bt.feeds.GenericCSVData(dataname="binance_data.csv", dtformat="%Y-%m-%d")

cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
cerebro.run()
cerebro.plot()
