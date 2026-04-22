# Binance Futures Testnet Trading Bot

## Setup

1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create .env file:
   API_KEY=your_api_key
   API_SECRET=your_secret

## Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features
- Market & Limit Orders
- BUY / SELL support
- CLI interface
- Logging (trading_bot.log)
- Error handling

## Assumptions
- Binance Futures Testnet is used
- User provides correct precision
