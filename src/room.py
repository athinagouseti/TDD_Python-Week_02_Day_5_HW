class Room:

    def __init__(self,capacity):
        self.songs = []
        self.guests = []
        self.capacity = capacity
    
    def total_guests(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if len(self.guests) < 4:
            self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
    def add_songs(self, song):
        self.songs.append(song)
        
    def guest_favourite_song_is_on(self, guest):
        for song in self.songs:
            if song.title == guest.favourite_song.title and song.artist == guest.favourite_song.artist:
                print(guest.favourite_song_is_on())
                return True
        return False

