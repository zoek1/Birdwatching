import web3
import json
import os

network = os.getenv('NETWORK_URL')
address = os.getenv('ADDRESS_NETWORK', '0xAf4Ef1a755F05DD9D68E9e53F111eb63b05fB1FD')
contract_path = os.getenv('CONTRACT_JSON_PATH', '../aave-protocol/build/contracts/LendingPoolCore.json')
abi =  json.load(open(contract_path))

w3 = web3.Web3(web3.HTTPProvider(network))
contract = w3.eth.contract(address=address, abi=abi["abi"])

user = ''
reserve ='0xFf795577d9AC8bD7D90Ee22b6C1703490b6512FD'

atokenintance = contract.functions.getReserveATokenAddress(reserve).call()
contract.functions.getReserveAvailableLiquidity(reserve).call()
contract.functions.getReserveInterestRateStrategyAddress(reserve).call()
contract.functions.getReserveTotalBorrows(reserve).call()
contract.functions.getReserveCurrentFixedBorrowRate(reserve).call()
contract.functions.getUserCurrentBorrowRateMode(reserve, user).call()




