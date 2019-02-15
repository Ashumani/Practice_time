from unit import Unit
from soldier import Soldier

class Archer(Unit):

    def __init__(self, *args, **kwargs):
        self.id = 2
        self.strong_against = [3, 5]

    def stronger_than(self, unit_id):
        return unit_id in self.strong_against