import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(4)
        self.room.songs = ["Little Lies", "I Want To Break Free", "Valerie"]
        
        self.guest_1 = Guest("Mick", 100, "Little Lies")
        self.guest_2 = Guest("Freddie", 50, "I Want To Break Free")
        self.guest_3 = Guest("Steven", 60, "Valerie")
        self.guest_4 = Guest("Brian", 40, "Hammer to Fall")
        self.guest_5 = Guest("Stevie", 30, "Hot Blooded")
        self.room.guests = [self.guest_1, self.guest_2, self.guest_3]
       
        
    def test_room_has_songs(self):
        self.assertEqual(["Little Lies", "I Want To Break Free","Valerie"], self.room.songs)

    def test_room_has_guests(self):
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room.guests)
    
    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_check_in_guest__have_capacity(self):
        self.room.check_in_guest(self.guest_4)
        self.assertEqual(4, len(self.room.guests))

    def test_check_in_guest__no_capacity(self):
        self.room.check_in_guest(self.guest_4)
        self.room.check_in_guest(self.guest_5)
        self.assertEqual(4, len(self.room.guests))

    def test_check_out_guests(self):
        self.room.check_out_guest(self.guest_3)
        self.assertEqual(2, len(self.room.guests))


    