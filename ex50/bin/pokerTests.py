from helpers import assertEqual, printFailures
from pokerFunction import *


# faces
assertEqual(2, face("2H"))
assertEqual(3, face("3D"))
assertEqual(13, face("KD"))
assertEqual(12, face("QD"))
assertEqual(14, face("AH"))
assertEqual(11, face("JH"))
assertEqual(10, face("10H"))
assertEqual(1, face("1H"))

# suits
assertEqual("H", suit("2H"))
assertEqual("D", suit("10D"))

#high card
assertEqual(14, highcard("2H 3D 6S 4C AC".split()))
assertEqual(14, highcard("AH 10D JS QC KC".split()))
assertEqual(14, highcard("AH 10D JS QC KC".split()))

#lowcard
assertEqual(2, lowcard("2H 3D 6S 4C AC".split()))
assertEqual(3, lowcard("6H 3D 6S 4C AC".split()))

# of a kind
assertEqual("2", ofAKind("2H", "2D"))
assertEqual("3", ofAKind("3H", "3D"))
assertEqual(False, ofAKind("3H", "2D"))
assertEqual("A", ofAKind("AH", "AD"))
assertEqual("10", ofAKind("10H", "10D"))

#card count
counts = cardCount("2H 3D 4S 5S 6D".split())
assertEqual(0, counts[0])
assertEqual(0, counts[1])
assertEqual(1, counts[2])
assertEqual(1, counts[3])
assertEqual(1, counts[4])
assertEqual(1, counts[5])
assertEqual(1, counts[6])
assertEqual(0, counts[7])

# canHasPairs
assertEqual(["3"], canHasPairs("2H 3H 3D 5H AD".split()))
assertEqual(["A"], canHasPairs("2H AH 3D 5H AD".split()))
assertEqual(["2", "A"], canHasPairs("2H AH 2D AH 8D".split()))
assertEqual([], canHasPairs("2H AH 3D 5H 8D".split()))

#threeOfAKind
assertEqual("3", threeOfAKind("2H 3H 3D 5H 3D".split()))
assertEqual("4", threeOfAKind("4H 4H 4D 5H 3D".split()))
assertEqual("Q", threeOfAKind("QH 3H QD 5H QS".split()))
assertEqual(False, threeOfAKind("3H 3H QD 5H QS".split()))

def tester(param):
    if param:
        return True
    else: return False

assertEqual(True, tester("no"))
assertEqual(True, tester("2"))

#fourOfAKind
assertEqual("3", fourOfAKind("2H 3H 3D 3H 3D".split()))
assertEqual("4", fourOfAKind("4C 4S 3D 4H 4D".split()))
assertEqual("4", fourOfAKind("4C 4D 4H 4S QD".split()))

#cheat (just because i can)
assertEqual("cheat", cheat("2H 2D 2D 2C 2H".split()))
assertEqual("cheat", cheat("2H 2D 2D 2C 2H 2K".split()))
assertEqual(False, cheat("2H 2D 2D 2C 3H".split()))

#full house
assertEqual("Full house", fullHouse("2H 2C 2D 3C 3S".split()))
assertEqual(False, fullHouse("2H 2D 2D 2C 2H".split()))
assertEqual(False, fullHouse("2H 2C 5D 3C 3S".split()))

#two pair
assertEqual("Two pair", twoPair("2H 2C 5D 3C 3S".split()))
assertEqual(False, twoPair("2H 2C 4D 5C AS".split()))
assertEqual(False, twoPair("7H 2C 4D 5C AS".split()))

#straight
assertEqual("7", straight("7H 6C 4D 5C 3S".split()))
assertEqual(False, straight("7H 7C 3D 5C 3S".split()))
assertEqual(False, straight("7H 7C 3D 7C 3S".split()))
assertEqual(False, straight("7H 7C 7D 5C 3S".split()))
assertEqual(False, straight("7H 7C 7D 7C 3S".split()))

#print failures
print printFailures()