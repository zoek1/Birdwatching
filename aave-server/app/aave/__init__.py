import json
import os

import web3


LENDING_POOL_JSON_PATH = '../aave-protocol/build/contracts/LendingPool.json'
LENDING_POOL_CORE_JSON_PATH = '../../aave-protocol/build/contracts/LendingPoolCore.json'
ATOKEN_JSON_PATH = '../../aave-protocol/build/contracts/AToken.json'


LENDING_POOL_ADDRESS = '0xB36017F5aafDE1a9462959f0e53866433D373404'
LENDING_POOL_CORE_ADDRESS = '0xAf4Ef1a755F05DD9D68E9e53F111eb63b05fB1FD'

RESERVES = {
    '0x3F80c39c0b96A0945f9F0E9f55d8A8891c5671A8': {
        'address': '0x3F80c39c0b96A0945f9F0E9f55d8A8891c5671A8',
        'name': 'Kyber Network ',
        'decimals': '',
        'symbol': 'KNC'
    },
    '0x260071C8D61DAf730758f8BD0d6370353956AE0E': {
        'address': '0x260071C8D61DAf730758f8BD0d6370353956AE0E',
        'name': 'Augur',
        'decimals': '',
        'symbol': 'REP'
    },
    '0x61e4CAE3DA7FD189e52a4879C7B8067D7C2Cc0FA': {
        'address': '0x61e4CAE3DA7FD189e52a4879C7B8067D7C2Cc0FA',
        'name': 'Maker',
        'decimals': '',
        'symbol': 'MKR'
    },
    '0xD0d76886cF8D952ca26177EB7CfDf83bad08C00C': {
        'address': '0xD0d76886cF8D952ca26177EB7CfDf83bad08C00C',
        'name': '0x Coin',
        'decimals': '',
        'symbol': 'ZRX'
    },
    '0x1BCe8A0757B7315b74bA1C7A731197295ca4747a': {
        'address': '0x1BCe8A0757B7315b74bA1C7A731197295ca4747a',
        'name': 'LEND',
        'decimals': '',
        'symbol': 'LEND'
    },
    '0x2d12186Fbb9f9a8C28B3FfdD4c42920f8539D738': {
        'address': '0x2d12186Fbb9f9a8C28B3FfdD4c42920f8539D738',
        'name': 'Basic Attention Token',
        'decimals': '',
        'symbol': 'BAT'
    },
    '0x1c4a937d171752e1313D70fb16Ae2ea02f86303e': {
        'address': '0x1c4a937d171752e1313D70fb16Ae2ea02f86303e',
        'name': 'TrueUSD',
        'decimals': '',
        'symbol': 'TUSD'
    },
    '0xFf795577d9AC8bD7D90Ee22b6C1703490b6512FD': {
        'address': '0xFf795577d9AC8bD7D90Ee22b6C1703490b6512FD',
        'name': 'DAI',
        'decimals': '',
        'symbol': 'DAI'
    },
    '0xd2eC3a70EF3275459f5c7a1d5930E9024bA3c4f3': {
        'address': '0xd2eC3a70EF3275459f5c7a1d5930E9024bA3c4f3',
        'name': 'Ampleforth',
        'decimals': '',
        'symbol': 'AMPL'
    },
    '0xe22da380ee6B445bb8273C81944ADEB6E8450422': {
        'address': '0xe22da380ee6B445bb8273C81944ADEB6E8450422',
        'name': 'USD Coin',
        'decimals': '',
        'symbol': 'USDC'
    },
    '0xD868790F57B39C9B2B51b12de046975f986675f9': {
        'address': '0xD868790F57B39C9B2B51b12de046975f986675f9',
        'name': 'Synthetix USD',
        'decimals': '',
        'symbol': 'SUSD'
    },
    '0xAD5ce863aE3E4E9394Ab43d4ba0D80f419F61789': {
        'address': '0xAD5ce863aE3E4E9394Ab43d4ba0D80f419F61789',
        'name': 'ChainLink',
        'decimals': '',
        'symbol': 'LINK'
    },
    '0x13512979ADE267AB5100878E2e0f485B568328a4': {
        'address': '0x13512979ADE267AB5100878E2e0f485B568328a4',
        'name': 'USDT Coin',
        'decimals': '',
        'symbol': 'USDT'
    },
    '0x3b92f58feD223E2cB1bCe4c286BD97e42f2A12EA': {
        'address': '0x3b92f58feD223E2cB1bCe4c286BD97e42f2A12EA',
        'name': 'WBTC Coin',
        'decimals': '',
        'symbol': 'WBTC'
    },
    '0x804C0B38593796bD44126102C8b5e827Cf389D80': {
        'address': '0x804C0B38593796bD44126102C8b5e827Cf389D80',
        'name': 'Ethereum',
        'decimals': '',
        'symbol': 'ETH'
    },
    '0x738Dc6380157429e957d223e6333Dc385c85Fec7': {
        'address': '0x738Dc6380157429e957d223e6333Dc385c85Fec7',
        'name': 'Decentraland',
        'decimals': '',
        'symbol': 'MANA'
    },
}


def get_connection(network):
    return web3.Web3(web3.HTTPProvider(network))


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

def get_currency_from_address(currency):
    return RESERVES.get(currency, {
        'address': '',
        'name': 'UNKNOWN',
        'symbol': '',
        'decimal': 0
    })
