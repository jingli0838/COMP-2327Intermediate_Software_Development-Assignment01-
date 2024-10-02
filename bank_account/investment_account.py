"""
Description: {The InvestmentAccount class will extend the BankAccount class 
by adding attributes and method implementations specific to an Investment Account.}
Author: {Jing Li}
Date: 10/1/2024
"""
from abc import ABC
from datetime import date, timedelta

from bank_account.bank_account import BankAccount


class InvestmentAccount(BankAccount):
    """
    This is a class representing a investment account.

    Attributes:
        __management_fee(float): The management_fee is a float which stores a flat-rate fee the bank charges for managing an InvestmentAccount.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee:float):
        """
        Initializes an InvestmentAccount instance with an account number, client number, balance, date created, and management fee.

        Args:
           account_number (int): A unique number for a bank account.
            client_number (int): A unique number for a bank account.
            balance (float): The initial balance for the account. If the balance cannot be converted to a float, 
            the balance will be initialized to 0.
            data_created(date): The date when the bankaccount created. If the incoming value is not an instance of date,
            use the today() method of the date class to initialize the attribute representing the date created.
            management_fee (float): A flat-rate fee the bank charges for managing an InvestmentAccount.
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55

    def __str__(self):
        """
        A string representation of the InvestmentAccount instance.
        If the account is 10 years old or less, the management fee is displayed using currency formatting with two decimal places.
        If the account is more than 10 years old, the management fee is waived.

        Returns:
            _str_: A formatted string that includes the account's information of the superclass and the management fee status
        """

        if self._date_created >= self.TEN_YEARS_AGO:
            return super().__str__()+f'\nDate Created: {self._date_created} Management Fee: ${self.__management_fee} Account Type: Investment'
        else:
            return super().__str__()+f'\nDate Created: {self._date_created} Management Fee: Wavied Account Type: Investment'

    def get_service_charges(self) ->float:
        """
        Calculate service charges that a Investment Account will incur using a specific formula

        Returns:
            _float_: the calculated service charges of a investment account.
        """

        if self._date_created < self.TEN_YEARS_AGO:

            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee
            

        return service_charge
            





