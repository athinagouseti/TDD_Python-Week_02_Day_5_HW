from src.song import Song
import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(4)

        self.song = Song("Fleetwood Mac", "Little Lies")
        self.song_1 = Song("Queen", "I Want To Break Free")
        self.song_2 = Song("Journey", "Any Way You Want It")
        self.song_3 = Song("Aerosmith", "Walk This Way")
        self.room.songs = [self.song, self.song_1, self.song_2]
       
        self.guest_1 = Guest( "Stevie", 30, Song("Foreigner", "Hot Blooded"))
        self.guest_2 = Guest("Freddie", 50, Song("Queen", "I Want To Break Free"))
        self.guest_3 = Guest("Steve", 60, Song("Steve Winwood", "Valerie"))
        self.guest_4 = Guest("Brian", 40, Song("Queen", "Hammer to Fall"))
        self.guest_5 = Guest("Mick", 100, Song("Fleetwood Mac", "Little Lies"))
        self.room.guests = [self.guest_1, self.guest_2, self.guest_3]
       
        
    def test_room_has_songs(self):
        self.assertEqual([self.song, self.song_1, self.song_2], self.room.songs)

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

    def test_add_songs_to_room(self):
        self.room.add_songs(self.song_3)
        self.assertEqual([self.song, self.song_1, self.song_2, self.song_3], self.room.songs)
        
    def test_guest_favourite_song_is_on(self):
        self.assertEqual(True, self.room.guest_favourite_song_is_on(self.guest_2))

    def test_guest_favourite_song_is__not_on(self):
        self.assertEqual(False, self.room.guest_favourite_song_is_on(self.guest_1))
