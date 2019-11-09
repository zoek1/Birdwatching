from datetime import datetime

from ens.utils import to_utc_datetime

from aave import get_currency_from_address

ETHER = 1000000000000000000
GWEI = 1000000000

def date_str_from_transaction(transaction):
    return to_utc_datetime(transaction['args']['timestamp']).strftime('%Y-%m-%dT%H:%M:%S%z')


def hexbytes_to_string(hexbytes):
    return "".join(["{:02X}".format(b) for b in hexbytes])


def wei_to_ether(wei):
    return wei / ETHER


def wei_to_gwei(wei):
    return wei / GWEI


def ether_to_wei(wei):
    return wei * ETHER


def gwei_to_wei(wei):
    return wei * GWEI


def event_to_point(transaction):
    print(transaction)
    amount = {} if transaction['args'].get('_amount', None) is None else {
        '_amount': wei_to_ether(transaction['args']['_amount']),
        'amount': str(transaction['args']['_amount'])
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

    return {
        "measurement": transaction['event'],
        "tags": {
            'address': transaction['address'],
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