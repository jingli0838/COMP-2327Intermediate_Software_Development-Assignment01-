"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Jing Li}
Date: {9/8/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

from client.client import Client
import unittest


class TestClient(unittest.TestCase):
    #create a instance of Class Client
    def setUp(self):
        self.client = Client(123, "Lily", "Green", "lilygreen@gmail.com")

    def test_init_valid(self):
        self.assertEqual(self.client._Client__client_number, 123)
        self.assertEqual(self.client._Client__first_name, "Lily")
        self.assertEqual(self.client._Client__last_name, "Green")
        self.assertEqual(self.client._Client__email_address, "lilygreen@gmail.com")
    # test invalid client number
    def test_init_invalid_client_number_raises_value_Error(self):
        with self.assertRaises(ValueError):
            Client(None, "Lily", "Green", "lilygreen@gmail.com")
        
    # test when Attribute first_name is blank
    def test_init_invalid_first_name_raises_value_Error(self):
        with self.assertRaises(ValueError):
            Client(123, " ", "Green", "lilygreen@gmail.com")

    # test when Attribute last_name is blank
    def test_init_invalid_last_name_raises_value_Error(self):
        with self.assertRaises(ValueError):
            Client(123,"lily ", " ", "lilygreen@gmail.com")

    # test when Attribute email_address is invalid
    def test_init_invalid_email_address_sets_default_value(self):
        expected= "email@pixell-river.com" 
        client= Client(123,"Lily ", "Green", "lilygreengmail")
        self.assertEqual(client.email_address, expected)

    #test getter method
    def test_client_number_accessor(self):
        self.assertEqual(self.client.client_number, 123)
    def test_first_name_accessor(self):
        self.assertEqual(self.client.first_name, "Lily")
    def test_last_name_accessor(self):
        self.assertEqual(self.client.last_name, "Green")
    def test_email_address(self):
        self.assertEqual(self.client.email_address, "lilygreen@gmail.com")

    #test __str__ method
    def test_str(self):
        expected = "Green, Lily[123]-lilygreen@gmail.com"
        self.assertEqual(str(self.client), expected)

    



    