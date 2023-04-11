#!/usr/bin/env python3

import argparse
from datetime import datetime
import pytz
import sys

import krakenex
import pykrakenapi

kraken = pykrakenapi.KrakenAPI(krakenex.API())


def print_query(ticker: str, date: datetime):
    timestamp = datetime.timestamp(date)
    data_frame, _ = kraken.get_ohlc_data(ticker, interval=60 * 24, since=timestamp - 1)
    print(data_frame)
    result = data_frame.loc[data_frame["time"] == timestamp]["close"]
    print(result)


def iso8601_type(iso8601: str) -> datetime:
    return datetime.fromisoformat(iso8601).astimezone(pytz.UTC)


# Use `kraken_spot_price USDCUSD 2022-04-01T00:00+00:00` to query the USDC/USD price on
# April 1, 2023 (UTC). This query will only work until roughly April 1, 2025 (UTC) because
# Kraken only gives us 720 data points (= days).
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ticker")
    parser.add_argument("date", type=iso8601_type)
    args = parser.parse_args(sys.argv[1:])
    print_query(args.ticker, args.date)
