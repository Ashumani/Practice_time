from unit import Unit 
from archer import Archer

class Knight(Unit):
    
    def __init__(self, *args, **kwargs):
        self.id = 1
        self.strong_against = [2, 4]

    def stronger_than(self, unit_id):
        return  unit_id in self.strong_against


