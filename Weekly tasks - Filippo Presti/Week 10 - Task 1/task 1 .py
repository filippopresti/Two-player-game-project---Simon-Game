import random as r

class Die:
    set_of_random_numbers = []
    def __init__(self, n_sides: int, n_dice: int, n_rolls: int):
        # Run validations to the received arguments
        assert n_sides > 0, f'Number of sides {n_sides} is not greater than 0!'
        assert n_dice > 0, f'Number of dice {n_dice} is not greater than 0!'
        assert n_rolls > 0, f'Times die/dice should roll {n_rolls} is not greater than 0!'

        # Assign to self object
        self.n_sides = n_sides
        self.n_dice = n_dice
        self.n_rolls = n_rolls

    def roll(self):
        # Repeat for loop by how many time the die/dice should be rolled
        for i in range(self.n_rolls):
            #print(f'Roll {i+1}:')
            # Repeat for loop by number of dice to be displayed
            for die in range(self.n_dice):
                    Die.set_of_random_numbers.append(r.randint(1, self.n_sides))
            print(f'Roll {i+1}: {Die.set_of_random_numbers[i*self.n_dice:]}')
    
    def sum_die_number(self):
        dice_sum = 0
        for i in range(self.n_rolls):
            dice_sum = sum(Die.set_of_random_numbers[i*self.n_dice:i*self.n_dice+self.n_dice])
            print(f'Total Sum of Roll {i+1}: is {dice_sum}')
    
    def average_die_number(self):
        avg = 0
        for i in range(self.n_rolls):
            avg = (sum(Die.set_of_random_numbers[i*self.n_dice:i*self.n_dice+self.n_dice]))/self.n_dice
            print(f'Average of Roll {i+1}: is {"%.2f" % avg}')
            
#print(Die.generate_random_number(Die(int(input('Enter number of sides: ')), int(input('Enter number of dice: ')), int(input('Enter how many times the die/dice must roll: ')))))
die1 = Die(int(input('Enter number of sides: ')), int(input('Enter number of dice: ')), int(input('Enter how many times the die/dice must roll: ')))
##  print(f'Number of sides: {die1.n_sides}, Number of dice: {die1.n_dice}, Times die/dice should roll: {die1.n_rolls}.')
die1.roll()
die1.average_die_number()
die1.sum_die_number()


class Dice:
    set_of_random_numbers = []
    def __init__(self, n_sides: int):

        # Assign to self object
        self.n_sides = n_sides

    def roll(self):
            return r.randint(1, self.n_sides)
    
    def change_num_of_sides(self, sides):
        self.sides = sides
    
    def roll_multiple(self, times):
        result = []
        for i in range(0, times):
            result.append(self.roll)
        return result
    
die = Dice(6)

class SetOfDice:
    dice = []
    def __init__(self, dice):
        self.dice.append(dice)

    def add_dice(self, dice):
        self.dice.append(dice)
    
    def remove_dice(self, dice):
        self.dice


SetOfDice(die)

