import sys ; sys.path += ['.', '../..']
from CryptoCode import MT19937 as MT
from time import time
import random


"""
>>> Crack an MT19937 seed
"""

def unixTimeStamp():
    return int(time())

def returnWaitTime(a, b):
    return random.randint(a, b)

def wait(a, b):
    """
    Picks a random time between two points
    """

    # Simulates passing of time
    waitTime = random.randint(a, b)
    now = unixTimeStamp()
    then = now + waitTime
    return then

def brute(targetOutput, timeStamp):

    while True:
        m = MT.MT19937(timeStamp)

        output = m.getInt()
        if output == targetOutput:
            return timeStamp

        timeStamp -= 1

def task22():

    # Waits for a set period of time
    seed = wait(40, 1000)

    # Uses the current time stamp
    m = MT.MT19937(seed)

    # Waits again (Simulation requires the previous time to be added on)
    now = seed + returnWaitTime(40, 1000)

    # Grabs the first input, this will be our target
    firstOutput = m.getInt()

    # Brute forces the seed
    newSeed = brute(firstOutput, now)

    return seed, newSeed


if __name__ == "__main__":
    _, newSeed = task22()
    print(f"Seed found: {newSeed}")

