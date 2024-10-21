"""
Description: {The ChequingAccount class will extend the BankAccount class by adding
attributes and method implementations specific to a Chequing Account.A Chequing Account
is meant for a banking client who has frequent transactions of both deposits and withdraws.}
Author: {Jing Li}
Date: {10/1/2024}
"""
from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """
    This is a class representing a chequing account.

    Attributes:
        __overdraft_limit (float): The maximum amount a balance can be overdrawn (below 0.00) before overdraft fees are applied.If the incoming value cannot be converted to a float, 
        the attribute representing the overdraft limit should be set to -100 
        __overdraft_rate (float): The rate to which overdraft fees will be applied. If the incoming value cannot be converted to a float,
        the attribute representing the overdraft rate should be set to 0.05
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, overdraft_limit:float, overdraft_rate:float):
        """
        Initializes a ChequingAccount instance with overdraft_limit and overdraft_rate and other parameters inherited from subclass.

        Args:
            account_number (int): a unique number for a bank account.
            client_number (int): a unique number for a bank account.
            balance (float): The initial balance for the account. If the balance cannot be converted to a float, 
            the balance will be initialized to 0.
            data_created(date): The date when the bankaccount created. If the incoming value is not an instance of date,
            use the today() method of the date class to initialize the attribute representing the date created.
            overdraft_limit (float): The maximum amount a balance can be overdrawn (below 0.00) before overdraft fees are applied.
            overdraft_rate (float): The rate to which overdraft fees will be applied.
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.00

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05

        self.__overdraft_strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    def __str__(self):
        """
        a string that include all the arguments,formatted for readability

        Returns:
            _str_: a string return result in the format including all the arguments.
        """
        return super().__str__() +f'\nOverdraft Limit: ${self.__overdraft_limit} Overdraft Rate: {self.__overdraft_rate*100:.2f}% Account Type: Chequing'

    def get_service_charges(self) ->float:
        """
        Calculate service charges that a BankAccount will incur using a specific formula based on the type of BankAccount.

        Returns:
            _float_: the calculated service charges.
        """
        return self.__overdraft_strategy.calculate_service_charges(self)
        
            





        








