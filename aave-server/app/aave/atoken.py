class AToken:
    def __init__(self, network, address, abi):
        self.network = network
        self.address = address
        self.abi = abi
        self.contract = network.eth.contract(address=address, abi=abi)

    # Events
    def redeem(self, *args, from_block=0):
        return self.contract.events.Redeem.getLogs(*args, fromBlock=from_block)

    def mint_on_deposit(self, *args, from_block=0):
        return self.contract.events.mint_on_deposit.getLogs(*args, fromBlock=from_block)

    def burn_on_liquidation(self, *args, from_block=0):
        return self.contract.events.BurnOnLiquidation.getLogs(*args, fromBlock=from_block)

    def transfer_on_liquidation(self, *args, from_block=0):
        return self.contract.events.TransferOnLiquidation.getLogs(*args, fromBlock=from_block)

    def balance_transfer(self, *args, from_block=0):
        return self.contract.events.BalanceTransfer.getLogs(*args, fromBlock=from_block)

    # Functions
    def get_exchange_rate(self):
        return self.contract.functions.getExchangeRate().call()

    def balance_of_underlying(self, user):
        return self.contract.functions.balanceOfUnderlying(user).call()

    def atoken_amount_to_underlying_amount(self, amount):
        return self.contract.functions.aTokenAmountToUnderlyingAmount(amount).call()

    def underlying_amount_to_atoken_amount(self, amount):
        return self.contract.functions.underlyingAmountToATokenAmount(amount).call()





