from datetime import datetime

from coinmarketcap.clients import CoinMarketCapClient
from ens.utils import to_utc_datetime

from aave import get_currency_from_address

ETHER = 1000000000000000000
GWEI = 1000000000

def date_str_from_transaction(transaction):
    return to_utc_datetime(transaction['args']['timestamp']).strftime('%Y-%m-%dT%H:%M:%S%z')


def hexbytes_to_string(hexbytes):
    return "".join(["{:02X}".format(b) for b in hexbytes])


def wei_to_ether(wei, currency):
    lng = currency['decimals']
    div = '1' + ('0' * (lng-1))
    return wei / int(div)


def wei_to_gwei(wei):
    return wei / GWEI


def ether_to_wei(wei):
    return wei * ETHER


def gwei_to_wei(wei):
    return wei * GWEI


def event_to_point(transaction):
    client = CoinMarketCapClient()
    print(transaction)
    amount = {}
    if transaction['args'].get('_amount', None) is not None:
        _amount = wei_to_ether(transaction['args']['_amount'],
                               get_currency_from_address(transaction['args']['_reserve']))
        _id = get_currency_from_address(transaction['args']['_reserve'])
        usd = client.cryptocoin.get(coin_id=_id)['quotes']['USD']['price']
        amount = {
            '_amount': _amount,
            'amount': str(transaction['args']['_amount']),
            'usd': _amount * usd,
        }

    reserve =  {
        'currency': get_currency_from_address(transaction['args']['_reserve'])['name'],
        'symbol': get_currency_from_address(transaction['args']['_reserve'])['symbol'],
    }

    reserve_tag = {} if transaction['args'].get('_reserve', None) is None else {
        'currency': get_currency_from_address(transaction['args']['_reserve'])['name'],
        'symbol': get_currency_from_address(transaction['args']['_reserve'])['symbol'],
        'reserve': transaction['args']['_reserve']
    }
    time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z') if transaction['args'].get('timestamp', None) is None else date_str_from_transaction(transaction)
    user = {} if transaction['args'].get('_user', None) is None else {'user': transaction['args']['_user']}

    return {
        "measurement": transaction['event'],
        "tags": {
            'address': transaction['address'],
            **user,
            **reserve_tag
        },
        "time": time,
        "fields": {
            'logIndex': transaction['logIndex'],
            'transactionIndex': transaction['transactionIndex'],
            'transactionHash': hexbytes_to_string(transaction['transactionHash']),
            'address': transaction['address'],
            'blockHash': hexbytes_to_string(transaction['blockHash']),
            'blockNumber': transaction['blockNumber'],
            **transaction['args'],
            **reserve,
            **amount,
        }
    }


def get_last_block(client, serie):
    q_points = list(client.query('SELECT blockNumber FROM {} ORDER BY time DESC LIMIT 1 '.format(serie)).get_points())
    return 0 if len(q_points) == 0 else q_points[0]['blockNumber'] + 1