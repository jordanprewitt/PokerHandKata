from helpers import assertEqual, printFailures
from Poker_Faces_Suits import face, suit

#Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH

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

printFailures()