import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
import json
import os

from scripts.request_data import request_data as s_ra

from strategies.trend_following import TrendFollowing


## Get API Key and API Secret
def getAPI():
    with open(os.getcwd() + "/data/API/api.json") as f:
        data = json.loads(f)
    f.close()
    return data


data = getAPI()
client = Client(data["api_key"], data["api_secret"])
bsm = BinanceSocketManager(client)

engine = sqlalchemy.create_engine('sqlite:///BTCUSDTstream.db')

s_ra(bsm, engine)

test_trade = TrendFollowing(bsm, engine)
test_trade.start(0.001, 60, 0.001)
