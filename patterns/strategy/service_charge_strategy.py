
"""
Description: {description of the file.}
Author: {Jing Li}
"""

from abc import ABC, abstractmethod

from bank_account.bank_account import BankAccount


class ServiceChargeStrategy(ABC):
    """
    An abstract base class representing a strategy for calculating service charges on a bank account.

    Constants:
        BASE_SERVICE_CHARGE (float): The base service charge applied to accounts.
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        Abstract method to calculate the service charges for a given account.

        Args:
            account (BankAccount): The account for which the service charge is calculated.

        Returns:
            float: The calculated service charge.
        """
        pass
        