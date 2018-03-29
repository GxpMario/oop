
import numpy as np


class Dice():
    """ We are simulating a roll of a dice with possible outcomes ranging
    from first_num to last_num (inclusive) """

    def __init__(self, first_num=1, last_num=6):
        self.first_num = first_num
        self.last_num = last_num

    def __check_dice(self):
        """ private method to check the validity of the dice """
        if self.last_num >= self.first_num >= 0:
            return True
        else:
            return False

    def sides(self):
        if self.__check_dice():
            return "Our dice has {} sides". \
                format(self.last_num + 1 - self.first_num)
        else:
            return 'No sides'

    def roll(self):
        if self.__check_dice():
            return "You rolled a " + \
                str(np.random.choice(np.arange(self.first_num,
                                               self.last_num + 1)))
        else:
            return 'No roll'



