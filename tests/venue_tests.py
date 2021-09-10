import unittest

from src.guest import Guest
from src.venue import Venue

class TestVenue(unittest.TestCase):

    def setUp(self):    
        self.venue = Venue("Cosmopol", 500, 5)
        self.guest_1 = Guest("Mick", 100, "Little Lies")
        self.guest_2 = Guest("Freddie", 2, "I Want To Break Free")
        self.guest_3 = Guest("Steven", 60, "Valerie")
        self.guest_4 = Guest("Brian", 40, "Hammer to Fall")
        self.guest_5 = Guest("Stevie", 30, "Hot Blooded")
        

    def test_venue_has_name(self):
        self.assertEqual("Cosmopol", self.venue.name)
    
    def test_venue_has_till(self):
        self.assertEqual(500, self.venue.till)

    def test_venue_has_entry_fee(self):
        self.assertEqual(5, self.venue.entry_fee)
        
    def test_guests_can_pay_entry_fee(self):
        transaction_1 = self.venue.can_pay_entry_fee(self.guest_1)
        self.assertEqual(True, transaction_1 ) 
    
    def test_guests_cannot_pay_entry_fee(self):
        transaction_2 = self.venue.can_pay_entry_fee(self.guest_2)
        self.assertEqual(False, transaction_2 )
        
    def test_guests_pay_entry_fee(self):
        self.venue.accept_entry_fee(self.guest_1)
        self.assertEqual(95, self.guest_1.wallet)
        self.assertEqual(505, self.venue.till)
    
    

