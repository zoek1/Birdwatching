class LendingPool:
    def __init__(self, network, abi, address='0xAf4Ef1a755F05DD9D68E9e53F111eb63b05fB1FD'):
        self.network = network
        self.address = address
        self.abi = abi
        self.contract = network.eth.contract(address=address, abi=abi)

    # Functions
    def get_reserve_atoken_address(self, reserve):
        return self.contract.functions.getReserveATokenAddress(reserve).call()

    def get_reserve_available_liquidity(self, reserve):
        return self.contract.functions.getReserveAvailableLiquidity(reserve).call()

    def get_reserve_interest_rate_strategy_address(self, reserve):
        return self.contract.functions.getReserveInterestRateStrategyAddress(reserve).call()

    def get_reserve_total_borrows(self, reserve):
        return self.contract.functions.getReserveTotalBorrows(reserve).call()

    def get_reserve_current_fixed_borrow_rate(self, reserve):
        return self.contract.functions.getReserveCurrentFixedBorrowRate(reserve).call()

    def get_user_current_borrow_rate_mode(self, reserve):
        return self.contract.functions.getUserCurrentBorrowRateMode(reserve).call()





