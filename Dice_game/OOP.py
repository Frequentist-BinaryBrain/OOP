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

class Player:
    
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter=10 #it is initially 10
    
    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
        
    def decrement_counter(self):
        self._counter -= 1
    
    def roll_die(self):
        return self._die.roll() # we will call this roll from die class
   
# Testing Die class 
die_game = Die()

print(die_game.value)
die_game.roll()
print(die_game.value)

#Testing player class
print("Now testing Player class")
#first let's create die instance for the player instance we create
my_die = Die()

my_player = Player(die=my_die, is_computer=True)

print(my_player)
print(my_player.die)
print(my_player.is_computer)
print(my_player.counter)
my_player.increment_counter()
print(my_player.counter)
my_player.decrement_counter()
print(my_player.counter)
my_player.roll_die()
print("Die value : ", my_die.value)

