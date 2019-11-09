from os import environ

from invoke import task

from common.tasks import collect_deposits, collect_redeem_underlying, collect_borrow, collect_repay, \
    collect_liquidation_call, collect_swap, collect_flash_loan, collect_reserve_used_as_collateral_enabled, \
    collect_reserve_used_as_collateral_disabled
from db import get_influx_instance


@task(help={'name': "Name of the database to create"})
def create(c, name='aave'):
    db = get_influx_instance()
    db.create_database(name)
    print('Creating database {}, Done!'.format(name))


@task(post=[create],
      help={
          'name': "Name of the database to create"
      })
def clean(c, name='aave'):
    db = get_influx_instance()
    db.drop_database(name)
    print('Dropping database {}, Done!'.format(name))


@task
def seed(c, name='aave', network=environ.get('NETWORK_URL')):
    collect_deposits(network_url=network)
    collect_redeem_underlying(network_url=network)
    collect_borrow(network_url=network)
    collect_repay(network_url=network)
    collect_liquidation_call(network_url=network)
    collect_swap(network_url=network)
    collect_flash_loan(network_url=network)
    collect_reserve_used_as_collateral_enabled(network_url=network)
    collect_reserve_used_as_collateral_disabled(network_url=network)