import time
import pandas as pd
from binance.client import Client

API_KEY = "<BINANCE_API_KEY>"
API_SECRET = "<BINANCE_SECRET_KEY>"
client = Client(API_KEY, API_SECRET, testnet=True)  # Testnet mode

def get_historical_data(symbol="BTCUSDT", interval="1h", limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=["timestamp", "open", "high", "low", "close", "volume", "_", "_", "_", "_", "_", "_"])
    df["close"] = df["close"].astype(float)
    return df

# automatic trade:
def trade(symbol="BTCUSDT"):
    data = get_historical_data(symbol)
    last_close = data["close"].iloc[-1]
    print(f"Último preço: {last_close}")

    if last_close > data["close"].mean():
        print("🔼 Tendência de alta, comprando...")
        order = client.order_market_buy(symbol=symbol, quantity=0.001)
    else:
        print("🔽 Tendência de baixa, vendendo...")
        order = client.order_market_sell(symbol=symbol, quantity=0.001)

    print("Ordem executada:", order)

# Loop para operar a cada 1 minuto
while True:
    trade()
    time.sleep(60)
