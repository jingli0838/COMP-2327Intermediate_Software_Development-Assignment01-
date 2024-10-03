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
        #Arrange 
        self.savings_account = SavingsAccount(9483914, 345, 1559.49, date(2024, 1, 1), 50.0)

    def test_init_valid(self):
        #Act & Assert
        self.assertEqual(9483914, self.savings_account._BankAccount__account_number)
        self.assertEqual(345, self.savings_account._BankAccount__client_number)
        self.assertEqual(1559.49, self.savings_account._BankAccount__balance)
        self.assertEqual(date(2024, 1, 1), self.savings_account._date_created)
        self.assertEqual(50, self.savings_account._SavingsAccount__minimum_balance)

    def test_minimum_balance_invalid(self):
        #Arrange
        savings_account = SavingsAccount(9483914, 345, 1559.49, date(2024, 1, 1), "minimum")
        expected_result = 50.0
        #Act & Assert
        self.assertEqual(expected_result, savings_account._SavingsAccount__minimum_balance)


    def test_get_service_charges_with_balance_greater_than_minimum_balance(self):
        #Arrange
        expected_result = self.savings_account.BASE_SERVICE_CHARGE
        #Act & Assert
        self.assertEqual(expected_result, round(self.savings_account.get_service_charges(), 2))

    def test_get_service_charges_with_balance_equal_to_minimum_balance(self):
        #Arrange
        savings_account = SavingsAccount(9483914, 345, 50.0, date(2024, 1, 1), 50.0)
        expected_result = savings_account.BASE_SERVICE_CHARGE
        #Act & Assert
        self.assertEqual(expected_result, round(savings_account.get_service_charges(), 2))

    def test_get_service_charges_with_balance_less_than_minimum_balance(self):
        #Arrange
        savings_account = SavingsAccount(9483914, 345, 10.0, date(2024, 1, 1), 50.0)
        expected_result = savings_account.BASE_SERVICE_CHARGE * savings_account.SERVICE_CHARGE_PREMIUM
        #Act & Assert
        self.assertEqual(expected_result, round(savings_account.get_service_charges(), 2))

    def test_str(self):
        #Arrange
        expected = "Account Number:9483914 Balance:$1,559.49\nMinimum Balance: $50.0 Account Type: Savings"
        #Act & Assert
        self.assertEqual(expected, str(self.savings_account))
  
    