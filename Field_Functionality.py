import numpy as np


def initialize_gamefield():
    field = np.zeros(shape=(10, 9, 9), dtype=int)
    for i in range(1, 10):
        field[i, :, :] = i

    return field


def make_choice(field, cell, value):
    field[0, cell[0], cell[1]] = value
    field[1:, cell[0], cell[1]] = 0


def find_least_variations(field):
    pass

if __name__ == '__main__':
    print("Field functionality is here")
else:
    pass