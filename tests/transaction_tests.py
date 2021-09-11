import unittest

from src.transaction import Transaction
from src.guest import Guest


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mick", 100, "Little Lies")
        self.transaction = Transaction(5, self.guest, "entry_fee")
        

    def test_transaction_has_amount(self):
        self.assertEqual(5, self.transaction.amount)

    def test_transaction_has_guest(self):
        self.assertEqual(self.guest, self.transaction.guest)

    def test_transaction_has_type(self):
        self.assertEqual("entry_fee", self.transaction.type)
        

    