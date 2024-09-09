"""
Description: {description of the file.}
Author: {Jing Li}
"""
from numbers import Number
#import numbers


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
    def update_balance(self,amount):
        """
        update balance of bankaccount
        """
        try:
            self.__balance += float(amount)
        except ValueError as e:
            print(f"the balance is not updated due to{e}")
    #deposit method
    def deposit(self,amount):
        """
        Deposite amount:
        - Amount must be numeric
        - Amount must be positive
        - Add the amount to the balance
        """
        if not isinstance(amount,Number):
            raise ValueError(f"Deposit amount:{amount} must be numeric")
        elif amount <= 0:
            raise ValueError(f"Deposit amount:${amount:,.2f} must be positive")
        else:
            self.update_balance(amount)
    #withdraw method
    def withdraw(self,amount):
        """
        Withdraw amount:
        - Amount must be numeric
        - Amount must be positive 
        - Amount must not exceed the account balance
        - Subtract amount from balance
        """
        if not isinstance(amount,Number):
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



        






    
