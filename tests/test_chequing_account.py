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

        self.chequing_account = ChequingAccount(123, 456, 0.0, date(2024, 8, 1), -100.0, 0.05)
    
    def test_init_valid(self):

        self.assertEqual(123, self.chequing_account._BankAccount__account_number)
        self.assertEqual(456, self.chequing_account._BankAccount__client_number)
        self.assertEqual(0.0, self.chequing_account._BankAccount__balance)
        self.assertEqual(date(2024, 8, 1), self.chequing_account._date_created)
        self.assertEqual(-100.0, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_overdraft_limit_invalid(self):
        chequing_account = ChequingAccount(123, 456, 1000.0, date(2024, 8, 1), "overdraft", 0.05)
        self.assertEqual(-100.00, chequing_account._ChequingAccount__overdraft_limit)

    def test_overdraft_rate_invalid(self):
        chequing_account = ChequingAccount(123, 456, 1000.00, date(2024, 8, 1), -200.0, "rate")
        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_date_created_invalid(self):
        chequing_account = ChequingAccount(123, 456, -600.00, 8/1/2024, -100.0, 0.05)
        self.assertEqual(date(2024, 10, 1), chequing_account._date_created)

    def test_get_service_charges_with_balance_greater_than_overdraft_limit(self):
        self.assertEqual(self.chequing_account.BASE_SERVICE_CHARGE, round(self.chequing_account.get_service_charges(),2))

    def test_get_service_charges_with_balance_less_than_overdraft_limit(self):
        chequing_account = ChequingAccount(123, 456, -600.0, date(2024, 8, 1), -100.0, 0.05)
        self.assertAlmostEqual(25.5,round(chequing_account.get_service_charges(),2))

    def test_get_service_charges_with_balance_equals_to_overdraft_limit(self):
        chequing_account = ChequingAccount(123, 456, -100.0, date(2024, 8, 1), -100.0, 0.05)
        self.assertAlmostEqual(chequing_account.BASE_SERVICE_CHARGE, round(chequing_account.get_service_charges(),2))

    def test_str(self):
        expected = 'Account Number:123 Balance:$0.00\nOverdraft Limit: $-100.0 Overdraft Rate: 5.00% Account Type: Chequing'
        self.assertEqual(expected,str(self.chequing_account))

    
        

    

    

