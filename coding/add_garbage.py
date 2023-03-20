import random
from coding import garbage
from coding import sprite_group


class AddGarbage:
    def __init__(self, quantity=1):
        self.quantity = quantity

    def add(self):
        for i in range(self.quantity):
            x_pos = random.randint(1, 900)
            y_pos = random.randint(-1000, -100)
            garbage_object = garbage.Garbage(random.randint(1, 5), x=x_pos, y=y_pos)
            sprite_group.garbage_group.add(garbage_object)
