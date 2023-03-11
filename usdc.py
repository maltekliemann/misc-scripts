from datetime import datetime
import pytz

import krakenex
import pykrakenapi

kraken = pykrakenapi.KrakenAPI(krakenex.API())
time = datetime(2023, 4, 1, 0, 0, tzinfo=pytz.utc)
timestamp = datetime.timestamp(time)
data_frame, _ = kraken.get_ohlc_data("USDCUSD", interval=60 * 24, since=timestamp - 1)
print(data_frame)
result = data_frame.loc[data_frame["time"] == timestamp]["close"]
print(result)
