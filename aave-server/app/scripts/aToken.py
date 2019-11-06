import web3
import json
import os

network = os.getenv('NETWORK_URL')
address = os.getenv('ADDRESS_NETWORK', '0x8Ac14CE57A87A07A2F13c1797EfEEE8C0F8F571A') #  Aave Interest bearing DAI (aDAI)
contract_path = os.getenv('CONTRACT_JSON_PATH')
abi =  json.load(open(contract_path))

w3 = web3.Web3(web3.HTTPProvider(network))
contract = w3.eth.contract(address=address, abi=abi["abi"])
user = ''
value = 2497136333377069922779834
contract.events.Redeem.getLogs(fromBlock=0)
contract.events.MintOnDeposit.getLogs(fromBlock=0)
contract.events.BurnOnLiquidation.getLogs(fromBlock=0)
contract.events.TransferOnLiquidation.getLogs(fromBlock=0)
contract.events.BalanceTransfer.getLogs(fromBlock=0)

contract.functions.getExchangeRate().call()
contract.functions.balanceOfUnderlying(user).call()
contract.functions.aTokenAmountToUnderlyingAmount(value).call()
contract.functions.underlyingAmountToATokenAmount(value).call()





