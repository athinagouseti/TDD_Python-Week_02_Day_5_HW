import unittest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("The Who", "Teenage Wasteland")

    def test_song_has_title(self):
        self.assertEqual("Teenage Wasteland", self.song.title)
        
    def test_song_has_artist(self):
        self.assertEqual("The Who", self.song.artist)
