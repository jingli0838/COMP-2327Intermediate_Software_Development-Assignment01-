"""
Description: {Unit tests for the savings account.}
Author: {Jing Li}
Date : 10/2/2024
"""

from datetime import date
import unittest

from bank_account.savings_account import SavingsAccount


class Test(unittest.TestCase):

    def setUp(self):
        self.savings_account = SavingsAccount(9483914, 345, 1559.49, date(2024, 1, 1), 50.0)

    def test_init_valid(self):
        self.assertEqual(9483914, self.savings_account._BankAccount__account_number)
        self.assertEqual(345, self.savings_account._BankAccount__client_number)
        self.assertEqual(1559.49, self.savings_account._BankAccount__balance)
        self.assertEqual(date(2024, 1, 1), self.savings_account._date_created)
        self.assertEqual(50, self.savings_account._SavingsAccount__minimum_balance)

    def test_minimum_balance_invalid(self):
        savings_account = SavingsAccount(9483914, 345, 1559.49, date(2024, 1, 1), "minimum")
        self.assertEqual(50.0, savings_account._SavingsAccount__minimum_balance)


    def test_get_service_charges_with_balance_greater_than_minimum_balance(self):
        self.assertEqual(self.savings_account.BASE_SERVICE_CHARGE, round(self.savings_account.get_service_charges(), 2))

    def test_get_service_charges_with_balance_equal_to_minimum_balance(self):
        savings_account = SavingsAccount(9483914, 345, 50, date(2024, 1, 1), 50.0)
        self.assertEqual(savings_account.BASE_SERVICE_CHARGE, round(savings_account.get_service_charges(), 2))

    def test_get_service_charges_with_balance_less_than_minimum_balance(self):
        savings_account = SavingsAccount(9483914, 345, 10, date(2024, 1, 1), 50.0)
        self.assertEqual(1.00, round(savings_account.get_service_charges(), 2))

    def test_str(self):
        expected = "Account Number:9483914 Balance:$1,559.49\nMinimum Balance: $50.0 Account Type: Savings"
        self.assertEqual(expected, str(self.savings_account))
  
    