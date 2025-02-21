# Trading Bot BTC Binance Moving Average

## Author: Douglas Mendes

This project is a Bitcoin trading bot that generates buy/sell signals using the Simple Moving Average (SMA) strategy on the Binance platform. The bot is designed to operate automatically and can be used for both live trading and backtesting.

## Features

- **Live Trading**: The bot connects to the Binance API and executes trades based on the SMA strategy.
- **Backtesting**: The bot uses historical data to simulate trading and evaluate the performance of the strategy.
- **Simple Moving Average (SMA)**: The strategy is based on the comparison of the current price with the SMA to determine buy/sell signals.

## Files

- `main.py`: Contains the code for live trading using the Binance API.
- `backtest.py`: Contains the code for backtesting the SMA strategy using historical data.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing an overview of the project.

## Requirements

- Python 3.x
- pandas
- backtrader
- binance

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/douglasmendes/trading_bot_btc_binance_moving_average.git
    cd trading_bot_btc_binance_moving_average
    ```

2. Install the required packages:
    ```sh
    pip install pandas backtrader python-binance
    ```

## Usage

### Live Trading

1. Set your Binance API key and secret in main.py:
    ```python
    API_KEY = "<YOUR_BINANCE_API_KEY>"
    API_SECRET = "<YOUR_BINANCE_SECRET_KEY>"
    ```

2. Run the trading bot:
    ```sh
    python main.py
    ```

### Backtesting

1. Prepare your historical data in a CSV file (e.g., `binance_data.csv`).

2. Run the backtest:
    ```sh
    python backtest.py
    ```

## Disclaimer

This project is for educational purposes only. Trading cryptocurrencies involves significant risk and can result in substantial losses. Use this bot at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




