from unit import Unit


class Wizard(Unit):

    def __init__(self, *args, **kwargs):
        self.id = 5
        self.strong_against = [1, 3, 4]

    def stronger_than(self, unit_id):
        return unit_id in self.strong_against