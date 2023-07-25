from binance.client import Client
from binance.exceptions import BinanceAPIException
from datetime import datetime, timedelta
import time
import getpass


api_key = getpass.getpass('input key: ')
api_secret = getpass.getpass('input secret: ')
memo = getpass.getpass('input memo: ')
delta_time = 600  # seconds

client = Client(api_key, api_secret)

while 1:
    balance = int(float(client.get_asset_balance(asset='BTS')['free']))
    
    print(f'''
        ...
        Start transaction, your balance is {balance} BTS')
        ...
    ''')

    try:
        withdrawal = client.withdraw(
            coin='BTS',
            address='binance-bts-1-refill',
            amount=balance,
            addressTag=memo
            )
    except BinanceAPIException as e:
        print(e)
    else:
        print('Success')
    
    future_time = datetime.now() + timedelta(seconds=delta_time)

    print(f'next transaction will be at {future_time}')
    time.sleep(delta_time)

