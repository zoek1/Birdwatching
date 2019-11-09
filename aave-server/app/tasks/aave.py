from os import environ

from invoke import task

from aave import get_connection, get_lending_pool_abi, RESERVES
from aave.lending_pool import LendingPool


@task(help={'network': "URL network to connect"})
def reserves(c, network=environ.get('NETWORK_URL')):
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    for reserve in {deposit['args']['_reserve'] for deposit in lending.deposit()}:
        res = RESERVES.get(reserve, {'name': 'Unknown', 'symbol': '?'})
        print('{}: {}({})'.format(reserve, res['name'], res['symbol'],))

