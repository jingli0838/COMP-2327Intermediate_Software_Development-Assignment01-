"""
Description: this file is for BankAccount class.
Author: {Jing Li}
Date:9/10/2024
"""


class BankAccount:
    """
    This is a class representing a bank account.

    Attributes:
        __account_number (int): a unique number for a bank account.
        __client_number (int): a unique number for a clients number.
        __balance (float): the current balance of the account.
    """
    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        Initializes a BankAccount instance with an account number, client number, and balance.

        Args:
            account_number (int): a unique number for a bank account.
            client_number (int): a unique number for a bank account.
            balance (float): The initial balance for the account. If the balance cannot be converted to a float, 
            the balance will be initialized to 0.

        Raises:
            ValueError: If `account_number` is not an integer.
            ValueError: If `client_number` is not an integer.
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("account_number must be an integer")
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("client_number must be an integer")
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0
         
    @property
    def account_number(self) -> int:
        """
        get the account number

        Returns:
            int: account number
        """
        return self.__account_number
    @property
    def client_number(self) -> int:
        """
        get the client number

        Returns:
            int: client number
        """
        return self.__client_number
    @property
    def balance(self) -> float:
        """
        get the current balance

        Returns:
            float: current balance
        """
        return self.__balance
    
    #to update the balance accroding to the amount
    def update_balance(self, amount: float):
        """
        update the balance of the bank account by adding a specified amount

        Args:
            amount (float): this amount can be converted to a float and is supposed to be added to the current balance 
            .it can be positive and negative.

        Raises:
            ValueError: if the amount can not be converted to a float.
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
           raise ValueError(f"the balance is not updated due to invalid amount")
    
    def deposit(self, amount: float):
        """
        deposit a specified amount of money into the bank account
        Args:
            amount (float): The amount to deposit into the account. It must be a positive number.

        Raises:
            ValueError: if amount is not numeric
            ValueError: if amount is less than or equal to 0.
        """
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Deposit amount:{amount} must be numeric")
        elif amount <= 0:
            raise ValueError(f"Deposit amount:${amount:,.2f} must be positive")
        else:
            self.update_balance(amount)
    #withdraw method
    def withdraw(self, amount: float):
        """
        withdraws the specified amount from the bank account.

        Args:
            amount (_type_): The amount to withdraw from the bank account, and should be numeric and positive.
            The amount must not exceed the current balance.

        Raises:
            ValueError: if the amount is not a numeric
            ValueError: if the amount is less than or equal to 0
            ValueError: if the amount exceed the current account balance
        """
      
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Withdraw amount:{amount} must be numeric")
        elif amount <=0:
            raise ValueError(f"Withdraw amount:${amount:,.2f} must be positive")
        elif amount > self.balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.balance:,.2f}")
        else:
            self.update_balance(-amount)
     # __str__ method is defined to produce a string   
    def __str__(self):
        """
        a string that include the ccount number and the current balance,formatted for readability

        Returns:
            Str: a formated string that displays the ccount number and the current balance
        """
        return f"Account Number:{self.account_number} Balance:${self.balance:,.2f}"



        






    
