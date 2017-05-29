from helpers import assertEqual, printFailures
from pokerFunction import face, suit, rank, highCard, highCardWinner

#Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH

assertEqual("KD", highCard("2H 3D 5S 9C KD".split()))
assertEqual("AC", highCard("2H 3D 5S AC KD".split()))
assertEqual("White Wins: AH", highCardWinner("2H 3D 5S 9C KD".split(),
                                             "2C 3H 4S 8C AH".split()))
assertEqual("Black Wins: AH", highCardWinner("2H 3D 5S 9C AH".split(),
                                             "2C 3H 4S 8C QH".split()))


# ranking
assertEqual("3H", rank("2H", "3H"))
assertEqual("4H", rank ("4H", "3H"))

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