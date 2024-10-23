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
   

class DiceGame():

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
    
    def play(self):
        print("================================")
        print("🎲 Welcome to Roll the Dice! 🎲")
        print("================================")
        while True:
            self.play_round()
            # TODO: implement gameover

    def play_round(self):
        # Welcome the user
        print("------- New Round -------")
        input("Press any key to Roll the dice 🎲")

        #Roll te dice 
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #show the values
        print(f'Your dice: {player_value}')
        print(f'Computer dice: {computer_value}')

        #Determine Winner and Loser
        if player_value > computer_value:
            print("You won the round") 
            self._player.decrement_counter() # Winner
            self._computer.increment_counter() # Loser
        elif computer_value > player_value:
            print("The computer won the round")
            self._player.increment_counter() # Loser
            self._computer.decrement_counter() # Winner
        else:
            print("it is a TIE!!")

        print(f"Your counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")


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

#Testing DIceGmae class
print("Testing the DiceGame class")
player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

#Start the game
game.play()

