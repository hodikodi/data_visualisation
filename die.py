from random import randint

class Die:
    """A class representing a single die"""

<<<<<<< Updated upstream
    def __init__(self, num_sides=6):
=======
    def __init__(self, num_sides=5):
>>>>>>> Stashed changes
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides"""
        return randint(1, self.num_sides)