"""
Description: This file is about a class representing a strategy for calculating service charges based on whether an account's balance meets the minimum required balance.

Author: {Jing Li}
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    A class representing a strategy for calculating service charges based on whether an account's balance meets the minimum required balance.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): A premium multiplier for accounts that do not meet the minimum balance.
        __minimum_balance (float): The minimum balance required to avoid the premium service charge.
    """
    
    

    def __init__(self, minimum_balance:float):
        """
        Initializes the MinimumBalanceStrategy with the specified minimum balance.

        Args:
            minimum_balance (float): The minimum balance required to avoid the premium service charge.
        """

        self.__minimum_balance = minimum_balance
        self.SERVICE_CHARGE_PREMIUM = 2.0
    

    def calculate_service_charges(self, account:BankAccount):
        """
        Calculates the service charge for the given account based on its balance.

        Args:
            account (BankAccount): The account for which to calculate the service charges.

        Returns:
            float: The calculated service charge.
        """

        if account.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        
        return service_charge  

    
