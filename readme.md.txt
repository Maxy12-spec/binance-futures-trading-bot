# Binance Futures Trading Bot (CLI)

## 📌 Description
This is a CLI-based Python trading bot that simulates placing Market and Limit orders on Binance Futures Testnet.

The application supports user input via command line, performs validation, logs activity, and follows a modular structure.

Due to regional restrictions preventing access to Binance Futures Testnet, a mock API client is implemented to simulate order placement while preserving the real API structure.

---

## ⚙️ Features
- Market and Limit order support
- BUY and SELL operations
- CLI-based input (argparse)
- Input validation
- Logging of requests and responses
- Modular code structure

---

## 🧱 Project Structure
trading_bot/
  bot/
    __init__.py
    client.py        # Binance client wrapper
    orders.py        # order placement logic
    validators.py    # input validation
    logging_config.py
  cli.py             # CLI entry point
  README.md
  requirements.txt
