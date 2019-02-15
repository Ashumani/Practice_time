from unit import Unit


class Seige(Unit):

    def __init__(self, *args, **kwargs):
        self.id = 4
        self.strong_against = [2, 3]

    def stronger_than(self, unit_id):
        return unit_id in self.strong_against