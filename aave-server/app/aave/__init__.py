import json

LENDING_POOL_JSON_PATH = '../../aave-protocol/build/contracts/LendingPool.json'
LENDING_POOL_CORE_JSON_PATH = '../../aave-protocol/build/contracts/LendingPoolCore.json'
ATOKEN_JSON_PATH = '../../aave-protocol/build/contracts/AToken.json'


LENDING_POOL_ADDRESS = '0xB36017F5aafDE1a9462959f0e53866433D373404'
LENDING_POOL_CORE_ADDRESS = '0xAf4Ef1a755F05DD9D68E9e53F111eb63b05fB1FD'

RESERVES = {
    'DAI': {
        'address': '',
        'symbol': 'DAI',
        'decimal': 0
    }
}


def get_lending_pool_abi():
    return json.load(open(LENDING_POOL_JSON_PATH))['abi']


def get_lending_pool_core_abi():
    return json.load(open(LENDING_POOL_CORE_JSON_PATH))['abi']


def get_atoken_abi():
    return json.load(open(ATOKEN_JSON_PATH))['abi']


def populate(network):
    from aave.LendingPoolCore import LendingPool

    lending_core = LendingPool(network, get_lending_pool_abi(), LENDING_POOL_CORE_ADDRESS)

    for key, value in RESERVES.items():
        value['atoken'] = lending_core.get_reserve_atoken_address(value['address'])