import ccxt
import json

#####################################################
symbol="BTC/USDT"
usd_size = 1000
price = 44000
trade = False
#####################################################

conf_file = ("conf.json")
with open(conf_file, 'r') as myfile:
    data = myfile.read()
    configs = json.loads(data)


binance_spot = ccxt.binance({
    'apiKey': configs["API_KEY"],
    'secret': configs["SECRET_KEY"]
    })


binance_futures = ccxt.binance({
    'apiKey': configs["API_KEY"],
    'secret': configs["SECRET_KEY"],
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future', 
    }
    })
    
try:
    if trade:
        trade_amount = round(1000/44000,4)
        print(f"Create limit orders for {symbol} @{price} for {trade_amount} size")
        binance_spot.create_limit_buy_order(symbol, trade_amount, price)
        binance_futures.create_limit_sell_order(symbol, trade_amount, price)

        print("##### Orders ########")
        binance_spot.fetch_orders(symbol)
        binance_futures.fetch_orders(symbol)
except Exception as e:
    print(e)

