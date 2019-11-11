import re
from datetime import timedelta, datetime
from os import environ

from safe_cast import safe_int
from sanic import Sanic
from sanic.response import json

from common.tasks import collect_deposits, collect_redeem_underlying, collect_borrow, collect_repay, \
    collect_liquidation_call, collect_swap, collect_flash_loan, collect_reserve_used_as_collateral_enabled, \
    collect_reserve_used_as_collateral_disabled
from common.tasks import app as scheduler
from db import get_influx_instance
from macros.db import build_query, get_wheres
from sanic_cors import CORS, cross_origin

NETWORK_URL = environ.get('NETWORK_URL')


app = Sanic()
CORS(app)


@app.route("/db/update/force", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/deposit", methods=['GET', 'OPTIONS'])
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

@app.route("/lending/redeem_underlying", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/borrow", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/repay", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/liquidation_call", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/swap", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/flash_loan", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/reserve_used_as_collateral_enabled", methods=['GET', 'OPTIONS'])
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


@app.route("/lending/reserve_used_as_collateral_disabled", methods=['GET', 'OPTIONS'])
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

@app.route("/lending/user", methods=['GET', 'OPTIONS'])
async def user_info(request):
    user = request.args.get('user', '')
    client = get_influx_instance()
    where = [{
        'key': '_user', 'value': user, 'type': 'eq'
    }]
    group = 'currency'
    select = '_amount__sum,currency__last,symbol__last'
    select_fee = '_amount__sum,_fee__sum'

    deposits = build_query('Deposit', where=where)
    redeem = build_query('RedeemUnderlying', where=where)
    borrow = build_query('Borrow', where=where)
    repay = build_query('Repay', where=where)
    swap = build_query('Swap', where=where)
    flash = build_query('FlashLoan',  where=where)
    reserveusedascollateralenabled = build_query('ReserveUsedAsCollateralEnabled', where=where)
    reserveusedascollateraldisabled = build_query('ReserveUsedAsCollateralDisabled', where=where)


    deposits_c = build_query('Deposit', where=where, group=group, select=select)
    redeem_c = build_query('RedeemUnderlying', where=where, group=group, select=select)
    borrow_c = build_query('Borrow', where=where, group=group, select=select)
    repay_c = build_query('Repay', where=where, group=group, select=select)
    flash_c = build_query('FlashLoan',  where=where, group=group, select=select_fee)

    return json({
        'user': user,
        'deposits': list(client.query(deposits.get_sql()).get_points()),
        'redeem': list(client.query(redeem.get_sql()).get_points()),
        'borrow': list(client.query(borrow.get_sql()).get_points()),
        'swap': list(client.query(swap.get_sql()).get_points()),
        'flash': list(client.query(flash.get_sql()).get_points()),
        'repay': list(client.query(repay.get_sql()).get_points()),
        'reserveusedascollateralenabled': list(client.query(reserveusedascollateralenabled.get_sql()).get_points()),
        'reserveusedascollateraldisabled': list(client.query(reserveusedascollateraldisabled.get_sql()).get_points()),
        'totals': {
            'deposits': list(client.query(deposits_c.get_sql()).get_points()),
            'redeem': list(client.query(redeem_c.get_sql()).get_points()),
            'borrow': list(client.query(borrow_c.get_sql()).get_points()),
            'repay': list(client.query(repay_c.get_sql()).get_points()),
            'flash': list(client.query(flash_c.get_sql()).get_points()),
        }
    })


@app.route("/lending/users", methods=['GET', 'OPTIONS'])
async def list_users(request):
    client = get_influx_instance()
    group = 'user'
    select = '_user__count,_user__last,_amount__sum'

    deposits = build_query('Deposit', group=group, select=select)
    redeem = build_query('RedeemUnderlying', group=group, select=select)
    borrow = build_query('Borrow', group=group, select=select)
    repay = build_query('Repay', group=group, select=select)

    users = {}

    for event in list(client.query(deposits.get_sql()).get_points()):
        if not users.get(event['last'], False):
            users[event['last']] = {'user': event['last'],'deposit': {}, 'redeem': {}, 'borrow': {}, 'repay': {}}
        users[event['last']]['deposit']['total'] = event['sum']
        users[event['last']]['deposit']['times'] = event['count']

    for event in list(client.query(redeem.get_sql()).get_points()):
        if not users.get(event['last'], False):
            users[event['last']] = {'user': event['last'],'deposit': {}, 'redeem': {}, 'borrow': {}, 'repay': {}}
        users[event['last']]['redeem']['total'] = event['sum']
        users[event['last']]['redeem']['times'] = event['count']

    for event in list(client.query(borrow.get_sql()).get_points()):
        if not users.get(event['last'], False):
            users[event['last']] = {'user': event['last'],'deposit': {}, 'redeem': {}, 'borrow': {}, 'repay': {}}
        users[event['last']]['borrow']['total'] = event['sum']
        users[event['last']]['borrow']['times'] = event['count']

    for event in list(client.query(repay.get_sql()).get_points()):
        if not users.get(event['last'], False):
            users[event['last']] = {'user': event['last'],'deposit': {}, 'redeem': {}, 'borrow': {}, 'repay': {}}
        users[event['last']]['repay']['total'] = event['sum']
        users[event['last']]['repay']['times'] = event['count']

    return json({
        'data': users.values()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
