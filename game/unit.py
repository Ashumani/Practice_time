# Unit class will be the base class for all units 
# all other pieces will inherit from base Unit class 
# each unit will have some unique properties 
# which we can define in inherit class

# TODO: create a unit class which will work as a base class for different units
# TODO: create instance varibles which will save the state the of that unit
# TODO: action the unit will perform will defined here. the inherited class will perform the action according to its choice
 
class Unit(object):

    def __init__(self, *args, **kwargs):
        pass
        
    def __str__(self):
        return self.__class__.__name__