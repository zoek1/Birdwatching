import re
from datetime import timedelta, datetime
from os import environ

from safe_cast import safe_int
from sanic import Sanic
from sanic.response import json

from common.tasks import collect_deposits, collect_redeem_underlying, collect_borrow, collect_repay, \
    collect_liquidation_call, collect_swap, collect_flash_loan, collect_reserve_used_as_collateral_enabled, \
    collect_reserve_used_as_collateral_disabled
from db import get_influx_instance
from macros.db import build_query, get_wheres

NETWORK_URL = environ.get('NETWORK_URL')


app = Sanic()


@app.route("/db/update/force")
async def force_refresh(request):
    collect_deposits.delay(network_url=NETWORK_URL)
    collect_redeem_underlying.delay(network_url=NETWORK_URL)
    collect_borrow.delay(network_url=NETWORK_URL)
    collect_repay.delay(network_url=NETWORK_URL)
    collect_liquidation_call.delay(network_url=NETWORK_URL)
    collect_swap.delay(network_url=NETWORK_URL)
    collect_flash_loan.delay(network_url=NETWORK_URL)
    collect_reserve_used_as_collateral_enabled.delay(network_url=NETWORK_URL)
    collect_reserve_used_as_collateral_disabled.delay(network_url=NETWORK_URL)

    return json({"hello": "world"})


@app.route("/lending/deposit")
async def list_deposit(request):
    allowed_attr = ['amount', '_amount', '_reserve', '_user', 'currency', 'symbol']
    where_regex = re.compile(r'^({})(__(gte?|lte?|ne))?$'.format('|'.join(allowed_attr)))

    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('Deposit', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })

@app.route("/lending/redeem_underlying")
async def list_deposit(request):
    allowed_attr = ['amount', '_amount', '_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('RedeemUnderlying', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/borrow")
async def list_deposit(request):
    allowed_attr = ['amount', '_amount', '_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('Borrow', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/repay")
async def list_repay(request):
    allowed_attr = ['amount', '_amount', '_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('Repay', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/liquidation_call")
async def list_liquidation_call(request):
    allowed_attr = ['amount', '_amount', '_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('LiquidationCall', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/swap")
async def list_swap(request):
    allowed_attr = ['_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('Swap', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/flash_loan")
async def list_flash_loan(request):
    allowed_attr = ['_reserve', '_user', 'currency', 'symbol', '_amount', '_fee', '_target']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('FlashLoan', limit=limit, since=since, until=until, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/reserve_used_as_collateral_enabled")
async def list_reserve_used_as_collateral_enabled(request):
    allowed_attr = ['_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    until = request.args.get('until', datetime.now().strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('ReserveUsedAsCollateralEnabled', limit=limit, since=since, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })


@app.route("/lending/reserve_used_as_collateral_disabled")
async def list_reserve_used_as_collateral_enabled(request):
    allowed_attr = ['_reserve', '_user', 'currency', 'symbol']


    months_ago = datetime.now() - timedelta(days=365)
    select = request.args.get('select', '*')
    group = request.args.get('group', '')
    limit = safe_int(request.args.get('limit', 0), 0)
    since = request.args.get('since', months_ago.strftime('%Y-%m-%d'))
    order = request.args.get('order', 'asc')
    where = get_wheres(request.args, attrs=allowed_attr)
    print(where)

    client = get_influx_instance()
    query = build_query('ReserveUsedAsCollateralDisabled', limit=limit, since=since, order=order, select=select, where=where, group=group)

    return json({
        'data': list(client.query(query.get_sql()).get_points())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
