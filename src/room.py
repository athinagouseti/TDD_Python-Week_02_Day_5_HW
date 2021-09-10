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