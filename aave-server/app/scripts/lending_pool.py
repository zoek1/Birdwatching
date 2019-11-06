import web3
import json
import os

network = os.getenv('NETWORK_URL')
address = os.getenv('ADDRESS_NETWORK', '0xB36017F5aafDE1a9462959f0e53866433D373404')
contract_path = os.getenv('CONTRACT_JSON_PATH', '../aave-protocol/build/contracts/LendingPool.json')
abi =  json.load(open(contract_path))

w3 = web3.Web3(web3.HTTPProvider(network))
contract = w3.eth.contract(address=address, abi=abi["abi"])

deposits = lending_pool.contract.events.Deposit.getLogs(fromBlock=0)
redeem_underlying = lending_pool.contract.events.RedeemUnderlying.getLogs(fromBlock=0)
borrow = lending_pool.contract.events.Borrow.getLogs(fromBlock=0)
repay = lending_pool.contract.events.Repay.getLogs(fromBlock=0)
liquidation_call = lending_pool.contract.events.LiquidationCall.getLogs(fromBlock=0) # empty
swap = lending_pool.contract.events.Swap.getLogs(fromBlock=0)
flash_loan = lending_pool.contract.events.FlashLoan.getLogs(fromBlock=0) # empty
reserve_used_as_collateral_enabled = lending_pool.contract.events.ReserveUsedAsCollateralEnabled.getLogs(fromBlock=0)
reserve_used_as_collateral_disabled = lending_pool.contract.events.ReserveUsedAsCollateralDisabled.getLogs(fromBlock=0)

