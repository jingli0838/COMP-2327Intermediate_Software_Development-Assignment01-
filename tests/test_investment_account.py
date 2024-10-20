"""
Description: {Unit tests for the investment account.}
Author: {Jing Li}
Date : 10/1/2024
"""

from datetime import date
import unittest


from bank_account.investment_account import InvestmentAccount


class Test(unittest.TestCase):

    def setUp(self):
        #Arrange 
        self.investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2024, 1, 1), 1.99)
    
    def test_init_valid(self):
        #Act & Assert
        self.assertEqual(2341234, self.investment_account._BankAccount__account_number)
        self.assertEqual(456, self.investment_account._BankAccount__client_number)
        self.assertEqual(19329.21, self.investment_account._BankAccount__balance)
        self.assertEqual(date(2024, 1, 1), self.investment_account._date_created)
        self.assertEqual(1.99, self.investment_account._InvestmentAccount__management_fee)

    def test_management_fee_invalid(self):
        #Arrange
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2024, 1, 1), "fee")
        expected_result = 2.55       
        #Act & Assert
        self.assertEqual(expected_result, round(investment_account._InvestmentAccount__management_fee, 2))
        
    def test_get_service_charges_with_date_created_more_than_ten_years(self):
        #Arrange
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2013, 1, 1), 1.99)
        expected_result = investment_account.BASE_SERVICE_CHARGE
        #AcT & Assert
        self.assertEqual(expected_result, round(investment_account.get_service_charges(), 2))

    def test_get_service_charges_with_date_created_exactly_ten_years(self):
        #Arrange
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2014, 10, 8), 1.99)
        expected_service_charges = investment_account.BASE_SERVICE_CHARGE + investment_account._InvestmentAccount__management_fee
        #Act & Assert
        self.assertEqual(expected_service_charges, round(investment_account.get_service_charges(), 2))

    def test_get_service_charges_with_date_created_within_ten_years(self):
        #Arrange
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2015, 1, 1), 1.99)
        expected_service_charges = investment_account.BASE_SERVICE_CHARGE + investment_account._InvestmentAccount__management_fee
        #Act & Assert
        self.assertEqual(expected_service_charges, round(investment_account.get_service_charges(), 2))

    def test_str_with_date_created_more_than_ten_years(self):
        #Arrange
        investment_account = InvestmentAccount(2341234, 456, 19329.21, date(2013, 1, 1), 1.99)
        expected = "Account Number:2341234 Balance:$19,329.21\nDate Created: 2013-01-01 Management Fee: Waived Account Type: Investment"
        #Act & Assert
        self.assertEqual(expected, str(investment_account))

    def test_str_with_date_created_within_ten_years(self):
        #Arrange
        expected = "Account Number:2341234 Balance:$19,329.21\nDate Created: 2024-01-01 Management Fee: $1.99 Account Type: Investment"
        #Act & Assert
        self.assertEqual(expected, str(self.investment_account))


    





