"""
Description: {description of the file.}
Author: {Jing Li}
"""

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating service charges based on account creation date and a management fee.
    
    Attributes:
        TEN_YEARS_AGO (date): A constant representing a date ten years ago from today.
        __date_created (date): The date the account was created.
        __management_fee (float): The management fee to apply.
    """
    def __init__(self, date_created:date, management_fee:float):
        """
        Initializes the ManagementFeeStrategy with the given creation date and management fee.
        
        Args:
            date_created (date): The date the account was created.
            management_fee (float): The management fee to apply.
        """

        self.__date_created = date_created
        self.__management_fee = management_fee

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def calculate_service_charges(self, account:BankAccount):
        """
        Calculates the service charge for the given account based on its creation date.
        
        Args:
            account (BankAccount): The account for which to calculate the service charges.
        
        Returns:
            float: The calculated service charge.
        """

        if account._date_created < self.TEN_YEARS_AGO:

            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee
            
        return service_charge
        