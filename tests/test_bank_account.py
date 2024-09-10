"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Jing Li}
Date: {9/9/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account= BankAccount(123,456,1000.00)
    
    def test_init_valid(self):
        self.assertEqual(self.bank_account._BankAccount__account_number,123)
        self.assertEqual(self.bank_account._BankAccount__client_number,456)
        self.assertEqual(self.bank_account._BankAccount__balance,1000.00)
    #test when bank_account is a string
    def test_bank_account_invalid(self):
        with self.assertRaises(ValueError):
            bank_account= BankAccount("123",456,1000.00)
    #test when client_account is a string
    def test_client_account_invalid(self):
        with self.assertRaises(ValueError):
            bank_account = BankAccount(123,"456",1000.00)
    #test when balance is an integer
    def test_balance_integer_converted_into_float(self):
        bank_account= BankAccount(123,456,1000)
        self.assertIsInstance(bank_account.balance,float)

    #test whent balance is a string and be setted to 0.0
    def test_balance_invalid(self):
        bank_account= BankAccount(123,456,"balance")
        expected = 0.0
        self.assertEqual(expected, bank_account.balance)
    
    #test getter method
    def test_account_number_accessor(self):
        self.assertEqual(123,self.bank_account.account_number)
    
    def test_client_number_accessor(self):
        self.assertEqual(456,self.bank_account.client_number)

    def test_balance(self):
        self.assertEqual(1000.00,round(self.bank_account.balance,2))

    #test update method when amount is positive
    def test_update_balance_with_positive_amount(self):
        self.bank_account.update_balance(200)
        expected = 1200.00
        self.assertEqual(expected,round(self.bank_account.balance,2))

    #test update method when amount is negative
    def test_update_balance_with_negative_amount(self):
        self.bank_account.update_balance(-200)
        expected =800.00
        self.assertEqual(expected,round(self.bank_account.balance,2))

    #test update method when amount is a string
    def test_update_amount_invalid(self):
        with self.assertRaises(ValueError):
            self.bank_account.update_balance("amount")
            
    #test deposit method when amount is a string
    def test_deposit_amount_invalid(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit("amount")
    #test deposit method when amount is negative
    def test_deposit_amount_negative(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-200)
    #test deposit amount is valid
    def test_deposit_amount_valid(self):
        self.bank_account.deposit(200)
        expected =1200.00
        self.assertEqual(expected,round(self.bank_account.balance,2))

    #test withdraw method, amount is invalid
    def test_withdraw_amount_invalid(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("amount")
    #test withdraw method, amount is not positive
    def test_withdraw_not_positive(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(0)
    #test withdraw method, amount is larger than current balance
    def test_withdraw_larger_than_balance(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(1100)

    #test withdraw amount is valid
    def test_withdraw_amount_valid(self):
        self.bank_account.withdraw(200)
        expected = 800
        self.assertEqual(expected,round(self.bank_account.balance,2))

    #test string method
    def test_string(self):
        expected = "Account Number:123 Balance:$1,000.00"
        self.assertEqual(expected,str(self.bank_account))








    
    





