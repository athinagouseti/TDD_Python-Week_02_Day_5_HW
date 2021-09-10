import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John", 50, "Hot Blooded")

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)
        
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Hot Blooded", self.guest.favourite_song)
    
    def test_favourite_song_is_on(self):
        self.assertEqual("Whoo", self.guest.favourite_song_is_on())
        