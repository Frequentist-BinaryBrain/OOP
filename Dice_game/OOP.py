import random


class Die:
    
    def __init__(self):
        self._value = None
        
    @property # We will write only getter for value because we don't want to set instead we use roll Method
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value
    

die_game = Die()

print(die_game.value)
die_game.roll()
print(die_game.value)