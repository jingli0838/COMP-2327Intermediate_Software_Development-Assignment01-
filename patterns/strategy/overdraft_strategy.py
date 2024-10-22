"""
Description: This file is about a class representing a strategy for calculating service charges based on overdraft limits and rates.
    
Author: {Jing Li}
"""
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating service charges based on overdraft limits and rates.
    
    Attributes:
        overdraft_limit (float): The overdraft limit of the account.
        overdraft_rate (float): The rate at which overdraft fees are applied.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with the specified overdraft limit and rate.
        
        Args:
            overdraft_limit (float): The overdraft limit of the account.
            overdraft_rate (float): The rate applied to overdraft amounts.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        Calculates the service charge for the given account based on its balance and overdraft.
        
        Args:
            account (BankAccount): The account for which to calculate the service charges.
        
        Returns:
            float: The calculated service charge.
        """
        
        if account.balance >= self.__overdraft_limit:

            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance) * self.__overdraft_rate

        return service_charge



       