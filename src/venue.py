class Venue:

    def __init__(self, name, till, entry_fee):
        self.name = name
        self.till = till
        self.entry_fee = entry_fee
        self.rooms = []
     
    def can_pay_entry_fee(self, guest):
        if guest.wallet > self.entry_fee:
            return True
        return False
    
    
    def accept_entry_fee(self, guest):
        if self.can_pay_entry_fee(guest) == True:
            self.till += self.entry_fee
            guest.wallet -= self.entry_fee
    
    

    

   

