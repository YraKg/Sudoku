import numpy as np
import enum

class Outcome(enum.Enum):
    SOLVED=0
    PROBLEM=1
    NOT_DONE_YET=2


def initializeGamefield():
    field = np.zeros(shape=(10, 9, 9), dtype=int)
    for i in range(1, 10):
        field[i, :, :] = i

    return field


def makeChoice(field, cell, value):
    field[0, cell[0], cell[1]] = value
    field[1:, cell[0], cell[1]] = 0


def findLeastVariations(field):
    counter=0
    min=[9,0,0] # min number + coordinates
    for i in range(0,9):
        for j in range(0,9):
            for x in field[1:,i,j]:
                if(x!=0):
                    counter=counter+1
            if(counter==1):
                return [i,j]
            if(counter<min and counter >0):
                min=[counter,i,j]

    return [min[1],min[2]]


def removeBadChoices(field,bad_moves):
    for move in bad_moves:
        field[move[0]][move[1]][move[2]]=0


def gameOver(field):
    solved=True
    for i in range(0,9):
        for j in range(0,9):

                if field[0,i,j] == 0:

                    solved=False

    if solved == True:

        return Outcome.SOLVED
    for i in range(0,9):
        for j in range(0,9):
            for x in field[1:, i, j]:

                if x != 0:

                    return Outcome.NOT_DONE_YET

    return Outcome.PROBLEM



if __name__ == '__main__':
    print("Field functionality is here")
else:
    pass