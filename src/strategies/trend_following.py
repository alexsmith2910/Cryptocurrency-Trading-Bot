import pandas as pd

## TrendFollowing
## -- if the crypto was rising by x % -> Buy
## -- exit when profit is above 0.15% or loss is crossing -0.15%

class TrendFollowing:
    def __init__(self, bsm, engine):
        self.bsm = bsm
        self.engine = engine

    def start(self, entry, lookback, qty, open_position=False):
        while True:
            df = pd.read_sql('BTCUSDT', self.engine)
            loopback_period = df.iloc[-lookback:]
            cumret = (loopback_period.Price.pct_change() + 1).cumprod() - 1
            if not open_position:
                if cumret[cumret.last_valid_index()] > entry:
                    order = client.create_order(symbol='BTCUSDT',
                                                side='BUY',
                                                type='MARKET',
                                                quantity=qty)
                    print(order)
                    open_position = True
                    break
        if open_position:
            while True:
                df = pd.read_sql('BTCUSDT', self.engine)
                since_buy = df.loc[df.Time >
                                    pd.to_datetime(order['transactTime'], unit='ms')]
                if len(since_buy) > 1:
                    since_buy_ret = (since_buy.Price.pct_change + 1).cumprod() - 1
                    last_entry = since_buy_ret[since_buy_ret.last_valid_index()]
                    if last_entry > 0.0015 or last_entry < -0.0015:
                        order = client.create_order(symbol='BTCUSDT',
                                                    side='SELL',
                                                    type='MARKET',
                                                    quantity=qty)
                        print(order)
                        break