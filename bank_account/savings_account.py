"""
Description: An Savings Account is meant for a banking client with a short-term savings plan. Typically the client will only deposit funds 
into a Savings Account but may occasionally make withdraws. The SavingsAccount class will extend the BankAccount class by adding attributes
and method implementations specific to a Savings Account.}
Author: {Jing Li}
Date: 10/2/2024
"""

from datetime import date
from bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    A class representing a saving account, inheriting from the BankAccount class.

    Attributes:
        __minimum_balance (float): The minimum value a balance can be before further service charges are applied.
    """

   
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """
        Initializes a SavingAccount instance with an account number, client number, balance, date created, and minimum balance.

        Args:
           account_number (int): A unique number for a bank account.
            client_number (int): A unique number for a bank account.
            balance (float): The initial balance for the account. If the balance cannot be converted to a float, 
            the balance will be initialized to 0.
            data_created(date): The date when the bankaccount created. If the incoming value is not an instance of date,
            use the today() method of the date class to initialize the attribute representing the date created.
            minimum_balance (float): The minimum value a balance can be before further service charges are applied. if invalid, it defaults to 50.
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.SERVICE_CHARGE_PREMIUM = 2.0 # a SavingsAccounts will incur 2 times the BASE_SERVICE_CHARGE when the balance drops below the minimum_balance.
        
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.0

    def __str__(self):
        """
        A string representation of the saving account instance.

        Returns:
            _str_: A formatted string that includes the account's balance, the minimum_balance and calculated service charges.
        """
        return super().__str__() + f'\nMinimum Balance: ${self.__minimum_balance} Account Type: Savings'
        
    def get_service_charges(self) -> float:
        """
        Calculate service charges that a Saving Account will incur using a specific formula

        Returns:
            _float_: the calculated service charges of a saving account.
        """
        if self.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        
        return service_charge
    







