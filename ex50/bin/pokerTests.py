from helpers import assertEqual, printFailures
from pokerFunction import face, suit, highcard, ofAKind, onePair, cardCount


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

# of a kind
assertEqual("2", ofAKind("2H", "2D"))
assertEqual("3", ofAKind("3H", "3D"))
assertEqual("no", ofAKind("3H", "2D"))
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

# of a pair
assertEqual("3", onePair("2H 3H 3D 5H AD".split()))
assertEqual("A", onePair("2H AH 3D 5H AD".split()))

#print failures
print printFailures()