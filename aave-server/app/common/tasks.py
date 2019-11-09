from celery import Celery
from os import environ

from influxdb import InfluxDBClient

from aave import get_connection, get_lending_pool_abi
from aave.lending_pool import LendingPool
from db import get_influx_instance
from macros.blockchain import event_to_point, get_last_block

REDIS_URI = environ.get("QUEUE_REDIS_URI", "127.0.0.1")
REDIS_PORT = environ.get("QUEUE_REDIS_PORT", "6379" )
REDIS_DB = environ.get("QUEUE_REDIS_DB", "0")


app = Celery("tasks", broker=f"redis://{REDIS_URI}:{REDIS_PORT}/{REDIS_DB}")
client = get_influx_instance()

@app.task
def run_task(*args, **kwargs):
  print('Hola desde el worker')


@app.task
def collect_deposits(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'Deposit')
    points = [event_to_point(deposit) for deposit in lending.deposit(from_block=block)]
    print(points)
    client.write_points(points)


@app.task
def collect_redeem_underlying(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'RedeemUnderlying')
    points = [event_to_point(event) for event in lending.redeem_underlying(from_block=block)]
    print(points)
    client.write_points(points)


@app.task
def collect_borrow(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'Borrow')
    points = [event_to_point(event) for event in lending.borrow(from_block=block)]
    print(points)
    client.write_points(points)


@app.task
def collect_repay(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'Repay')
    points = [event_to_point(event) for event in lending.repay(from_block=block)]
    print(points)
    client.write_points(points)


@app.task
def collect_liquidation_call(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'LiquidationCall')
    events = lending.liquidation_call(from_block=block)
    if len(events) > 0:
        points = [event_to_point(event) for event in events]
        print(points)
        client.write_points(points)
    else:
        print('No events for Liquidation Call')


@app.task
def collect_swap(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'Swap')
    events = lending.swap(from_block=block)
    if len(events) > 0:
        points = [event_to_point(event) for event in events]
        print(points)
        client.write_points(points)
    else:
        print('No events for Swap')


@app.task
def collect_flash_loan(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'FlashLoan')
    events = lending.flash_loan(from_block=block)
    if len(events) > 0:
        points = [event_to_point(event) for event in events]
        print(points)
        client.write_points(points)
    else:
        print('No events for Flash Loan')


@app.task
def collect_reserve_used_as_collateral_enabled(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'ReserveUsedAsCollateralEnabled')
    events = lending.reserve_used_as_collateral_enabled(from_block=block)
    if len(events) > 0:
        points = [event_to_point(event) for event in events]
        print(points)
        client.write_points(points)
    else:
        print('No events for Reserve Used As Collateral Enabled')

@app.task
def collect_reserve_used_as_collateral_disabled(*args, **kwargs):
    network = kwargs.get('network_url')
    conn = get_connection(network)
    lending = LendingPool(conn, get_lending_pool_abi())
    block = get_last_block(client, 'ReserveUsedAsCollateralDisabled')
    events = lending.reserve_used_as_collateral_disabled(from_block=block)
    if len(events) > 0:
        points = [event_to_point(event) for event in events]
        print(points)
        client.write_points(points)
    else:
        print('No events for Reserve Used As Collateral Enabled')
