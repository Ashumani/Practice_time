from unit import Unit
class Soldier(Unit): 

    def __init__(self, *args, **kwargs):
        self.id = 3
        self.strong_against = [1]

    def stronger_than(self, unit_id):
        return unit_id in self.strong_against


if __name__=="__main__":
    s = Soldier()
    print(str(s))