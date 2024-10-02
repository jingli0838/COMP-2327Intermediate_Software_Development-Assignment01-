"""
Description: {Unit tests for the chequing account.}
Author: {Jing Li}
Date : 10/1/2024
"""

from datetime import date
import unittest


from bank_account.investment_account import InvestmentAccount


class Test(unittest.TestCase):

    def setUp(self):
        self.investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2024, 1, 1), 1.99)
    
    def test_init_valid(self):
        self.assertEqual(2341234, self.investment_account._BankAccount__account_number)
        self.assertEqual(456, self.investment_account._BankAccount__client_number)
        self.assertEqual(19329.21, self.investment_account._BankAccount__balance)
        self.assertEqual(date(2024, 1, 1), self.investment_account._date_created)
        self.assertEqual(1.99, self.investment_account._InvestmentAccount__management_fee)

    def test_management_fee_invalid(self):
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2024, 1, 1), "fee")
        self.assertEqual(2.55, investment_account._InvestmentAccount__management_fee)
        
    def test_get_service_charges_with_date_created_more_than_ten_years(self):
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2013, 1, 1), 1.99)
        self.assertEqual(investment_account.BASE_SERVICE_CHARGE, investment_account.get_service_charges())

    def test_get_service_charges_with_date_created_exactly_ten_years(self):
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2014, 10, 3), 1.99)
        self.assertEqual(2.49, investment_account.get_service_charges())

    def test_get_service_charges_with_date_created_within_ten_years(self):
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2015, 1, 1), 1.99)
        self.assertEqual(2.49, investment_account.get_service_charges())

    def test_str_with_date_created_more_than_ten_years(self):
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2013, 1, 1), 1.99)
        expected = "Account Number:2341234 Balance:$19,329.21\nDate Created: 2013-01-01 Management Fee: Wavied Account Type: Investment"
        self.assertEqual(expected, str(investment_account))

    def test_str_with_date_created_within_ten_years(self):
        expected = "Account Number:2341234 Balance:$19,329.21\nDate Created: 2024-01-01 Management Fee: $1.99 Account Type: Investment"
        self.assertEqual(expected, str(self.investment_account))

    





