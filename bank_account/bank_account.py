"""
Description: {This module defines a `BankAccount` class, creating a simple bank account with an account number, 
client number, and balance. The class includes methods to deposit, withdraw, and update the balance, with validations
for numeric input and account balance limits. It also handles invalid input and ensures that the balance is always
valid. Additionally, the class provides string representation for displaying account information.}
Author: {Jing Li}
Date:9/10/2024
"""


class BankAccount:
    def __init__(self,account_number:int,client_number:int,balance:float):
        # check if account_number is integer
        if isinstance(account_number,int):
            self.__account_number = account_number
        else:
            raise ValueError("accoutn_number must be an integer")
        # check if client_number is integer
        if isinstance(client_number,int):
            self.__client_number =client_number
        else:
            raise ValueError("client_number must be an integer")
        # check if the value of balance can be successfully converted to a float. 
        # If the balance value cannot be converted to a float, the attribute representing the balance should be set to 0
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0
         
    @property
    def account_number(self)->int:
        return self.__account_number
    @property
    def client_number(self)->int:
        return self.__client_number
    @property
    def balance(self)->float:
        return self.__balance
    
    #to update the balance accroding to the amount
    def update_balance(self,amount:float):
        """
        update balance of bankaccount
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError:
           raise ValueError(f"the balance is not updated due to invalid amount")
    #deposit method
    def deposit(self,amount):
        """
        Deposite an amount into account

        Deposite amount:
        - Amount must be numeric
        - Amount must be positive

        if amount is valid, add the amount to the balance
        or else raise ValueError
        """
        if not isinstance(amount,(float,int)):
            raise ValueError(f"Deposit amount:{amount} must be numeric")
        elif amount <= 0:
            raise ValueError(f"Deposit amount:${amount:,.2f} must be positive")
        else:
            self.update_balance(amount)
    #withdraw method
    def withdraw(self,amount):
        """
        withdraw an amount from account

        Withdraw amount:
        - Amount must be numeric
        - Amount must be positive 
        - Amount must not exceed the account balance
        
        If amount is valid, Subtract amount from balance
        or else raise ValueError
        """
        if not isinstance(amount,(float,int)):
            raise ValueError(f"Withdraw amount:{amount} must be numeric")
        elif amount <=0:
            raise ValueError(f"Withdraw amount:${amount:,.2f} must be positive")
        elif amount > self.balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.balance:,.2f}")
        else:
            self.update_balance(-amount)
     # __str__ method is defined to produce a string   
    def __str__(self):
        return f"Account Number:{self.account_number} Balance:${self.balance:,.2f}"



        






    
