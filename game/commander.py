# commander class will stand as a base class for commander 
# You can create as much as many commandar you want from Commander class by inheriting it 
# Commander class will hold properties of a commander 
# Actions that commander can perform 

# TODO: Create a commander class and add methods as actions that can be done by commander 
class Commander(object):

    def __init__(self, *args, **kwargs):
        self.units = []
        self.total_money = 10
        self.money_spent = 0
        self._name = None 
        self._num_medics = 0
        
    def buy_units(self, unit, amount=1):
        for i in range(amount):
            self.units.append(unit)
        self.money_spent += amount
    
    def buy_medics(self):
        self.medics = self.total_money - self.money_spent

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def medics(self):
        return self._num_medics
    
    @medics.setter 
    def medics(self, num):
        self._num_medics = num

    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return "Object at {}".format(id(self))

    
        
    

        