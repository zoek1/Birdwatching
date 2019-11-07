class LendingPool:
    def __init__(self, network, abi, address='0xB36017F5aafDE1a9462959f0e53866433D373404'):
        self.network = network
        self.address = address
        self.abi = abi
        self.contract = network.eth.contract(address=address, abi=abi)

    def deposit(self, *args, from_block=0):
        return self.contract.events.Deposit.getLogs(*args, fromBlock=from_block)

    def redeem_underlying(self, *args, from_block=0):
        return self.contract.events.RedeemUnderlying.getLogs(*args, fromBlock=from_block)

    def borrow(self, *args, from_block=0):
        return self.contract.events.Borrow.getLogs(*args, fromBlock=from_block)

    def repay(self, *args, from_block=0):
        return self.contract.events.Repay.getLogs(*args, fromBlock=from_block)

    def liquidation_call(self, *args, from_block=0):
        return self.contract.events.LiquidationCall.getLogs(*args, fromBlock=from_block)

    def swap(self, *args, from_block=0):
        return self.contract.events.Swap.getLogs(*args, fromBlock=from_block)

    def flash_loan(self, *args, from_block=0):
        return self.contract.events.FlashLoan.getLogs(*args, fromBlock=from_block)

    def reserve_used_as_collateral_enabled(self, *args, from_block=0):
        return self.contract.events.ReserveUsedAsCollateralEnabled.getLogs(*args, fromBlock=from_block)

    def reserve_used_as_collateral_disabled(self, *args, from_block=0):
        return self.contract.events.ReserveUsedAsCollateralDisabled.getLogs(*args, fromBlock=from_block)
