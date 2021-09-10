class Venue:

    def __init__(self, name, till, entry_fee):
        self.name = name
        self.till = till
        self.entry_fee = entry_fee
        self.rooms = []
     

    def accept_entry_fee(self, guest):
        pass

    def can_pay_entry_fee(self, guest):
        pass

   

