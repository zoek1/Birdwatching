import web3
import json
import os

network = os.getenv('NETWORK_URL')
address = os.getenv('ADDRESS_NETWORK', '0x9C6C63aA0cD4557d7aE6D9306C06C093A2e35408')
contract_path = os.getenv('CONTRACT_JSON_PATH')
abi =  json.load(open(contract_path))

w3 = web3.Web3(web3.HTTPProvider(network))
contract = w3.eth.contract(address=address, abi=abi["abi"])

reserves = {
        '0x1BCe8A0757B7315b74bA1C7A731197295ca4747a': {
            name: 'LEND',
            abbrv: 'LEND'
            }
        }
lending_pool = contract.functions.getLendingPool().call()

