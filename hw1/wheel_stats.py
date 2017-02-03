# Requires Python3 to run
# Contains statistical Wheel of Fortune functions

import random
import sys

def spinUntilBankrup():
    """Simulates spinning in Wheel of Fortune until bankrupt is rolled.
    Returns the number of rounds (including round in which bankrupt is rolled)
    and the total accumulated."""

    rd = 0
    total = 0

    while True:
        spin = random.randrange(12)
        rd += 1

        if spin == 0:
            return [rd, total]
        else:
            total += 100 * spin

def spinFor(n):
    """Simulates spinning n times in Wheel of Fortune, or until bankrupt is
    rolled, whichever is first."""

    rd = 0
    total = 0

    while rd <= n:
        spin = random.randrange(12)
        rd += 1

        if spin == 0:
            total = 0
            return [rd, total]
        else:
            total += 100 * spin

    return [rd, total]

def spinUntil6600():
    """Simulates spinning in Wheel of Fortune until a sum of 6600 is obtained,
    or until bankrupt, whichever is first."""
    rd = 0
    total = 0

    while total <= 6600:
        spin = random.randrange(12)
        rd += 1

        if spin == 0:
            total = 0
            return [rd, total]
        else:
            total += 100 * spin

    return [rd, total]

def spinUntil6600AndFor12():
    """Simulates spinning in Wheel of Fortune until both a total of 6600 is
    obtained and 12 rounds have passed. Bankrupctcy ends this function."""
    rd = 0
    total = 0

    while total <= 6600 or rd <= 12:
        spin = random.randrange(12)
        rd += 1

        if spin == 0:
            total = 0
            return [rd, total]
        else:
            total += 100 * spin

    return [rd, total]

def nGames(n):
    """Simulates plaing n games of Wheel of Fortune.
    Returns the average number of rounds and average total gained."""

    avgRound = 0
    avgTotal = 0

    for i in range(n):
        #result = spinUntilBankrup()
        #result = spinFor(12)
        #result = spinUntil6600()
        result = spinUntil6600AndFor12()
        avgRound += result[0]
        avgTotal += result[1]

    return [(avgRound + 0.0) / n, (avgTotal + 0.0) / n]

for line in sys.stdin:
    numOfGames = int(line)
    print(nGames(numOfGames))
