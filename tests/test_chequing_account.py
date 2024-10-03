"""
Description: {Unit tests for the chequing account.}
Author: {Jing Li}
Date: 10/1/2024
"""


from datetime import date
import unittest

from bank_account.chequing_account import ChequingAccount


class Test(unittest.TestCase):

    def setUp(self):
        #Arrange 
        self.chequing_account = ChequingAccount(123, 456, 0.0, date(2024, 8, 1), -100.0, 0.05)
    
    def test_init_valid(self):
        #Act & Assert
        self.assertEqual(123, self.chequing_account._BankAccount__account_number)
        self.assertEqual(456, self.chequing_account._BankAccount__client_number)
        self.assertEqual(0.0, self.chequing_account._BankAccount__balance)
        self.assertEqual(date(2024, 8, 1), self.chequing_account._date_created)
        self.assertEqual(-100.0, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_overdraft_limit_invalid(self):
        #Arrange
        chequing_account = ChequingAccount(123, 456, 0.0, date(2024, 8, 1), "overdraft", 0.05)
        expected_result = -100.00
        #Act & Assert
        self.assertEqual(expected_result, chequing_account._ChequingAccount__overdraft_limit)

    def test_overdraft_rate_invalid(self):
        #Arrange
        chequing_account = ChequingAccount(123, 456, 0.00, date(2024, 8, 1), -100.0, "rate")
        expected_result = 0.05
        #Act & Assert
        self.assertEqual(expected_result, chequing_account._ChequingAccount__overdraft_rate)

    def test_date_created_invalid(self):
        #Arrange
        chequing_account = ChequingAccount(123, 456, -600.00, "invalid date", -100.0, 0.05)
        expected_result = date(2024, 10, 2)
        #Act & Assert
        self.assertEqual(expected_result, chequing_account._date_created)

    def test_get_service_charges_with_balance_greater_than_overdraft_limit(self):
        #Arrange
        expected_result = self.chequing_account.BASE_SERVICE_CHARGE
        #Act & Assert
        self.assertEqual(expected_result, round(self.chequing_account.get_service_charges(),2))

    def test_get_service_charges_with_balance_less_than_overdraft_limit(self):
        #Arrange
        chequing_account = ChequingAccount(123, 456, -600.0, date(2024, 8, 1), -100.0, 0.05)
        expected_result = chequing_account.BASE_SERVICE_CHARGE + (chequing_account._ChequingAccount__overdraft_limit - chequing_account.balance) * chequing_account._ChequingAccount__overdraft_rate
        #Act & Assert
        self.assertAlmostEqual(expected_result,round(chequing_account.get_service_charges(),2))

    def test_get_service_charges_with_balance_equals_to_overdraft_limit(self):
        #Arrange
        chequing_account = ChequingAccount(123, 456, -100.0, date(2024, 8, 1), -100.0, 0.05)
        expected_result = chequing_account.BASE_SERVICE_CHARGE
        #Act & Assert
        self.assertAlmostEqual(expected_result, round(chequing_account.get_service_charges(),2))

    def test_str(self):
        #Arrange
        expected_result = 'Account Number:123 Balance:$0.00\nOverdraft Limit: $-100.0 Overdraft Rate: 5.00% Account Type: Chequing'
        #Act & Assert
        self.assertEqual(expected_result,str(self.chequing_account))

    
        

    

    

