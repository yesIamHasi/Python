# Monte Carlo Simulation of Dice

import random

def dice(side, rolls): # rolls can't be zero.
    ''' Returns probability of a side in sample space of dice'''
    sample_space = []
    for i in range(1, rolls):
        sample_space.append( random.randint(0, rolls) )
    return float(sample_space.count(side)*100)/float(len(sample_space))

def average(_list):
    ''' Returns average of  an integer/float list '''
    counter = 0
    for i in _list:
        counter += i
    return float(counter)/len(_list)

if __main__ == '__name__':
    event = []
    for i in range(10000):
        # Find the probability of 1
        event.append(dice(1, 57))

    print average(event)
