from helpers import assertEqual, printFailures
from pokerFunction import face, suit, rank, highCard, highCardWinner, isTwoOfAKind, isThreeOfAKind,isFourOfAKind,isTwoPair, isFullHouse,  isFlush, isStraight, isStraightFlush, isRoyalFlush, identifyHand,  gameWinner

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

# of a kinds
assertEqual(2, isTwoOfAKind("2H 3D 5S 9C 2D".split()))
assertEqual(3, isTwoOfAKind("3H 3D 5S 9C 2D".split()))
assertEqual("No", isTwoOfAKind("3H 7D 5S 9C 2D".split()))
assertEqual("No", isTwoOfAKind("3H 3D 5S 9C 3D".split()))
assertEqual(2, isTwoOfAKind("5S 5C 5D 2H 2D".split()))

assertEqual(2, isThreeOfAKind("2H 2D 5S 9C 2D".split()))
assertEqual("No", isThreeOfAKind("2H 3D 5S 9C 6D".split()))
assertEqual("No", isThreeOfAKind("2H, 2D, 2C, 4H, 2S".split()))
    
assertEqual(2, isFourOfAKind("2H 2D 2S 9C 2D".split()))
assertEqual("No", isFourOfAKind("2H 3D 5S 9C 6D".split()))

assertEqual((2,5), isTwoPair("2H 2D 5S 5C 3D".split()))
assertEqual("No", isTwoPair("2H 2D 5S 6C 3D".split()))
assertEqual("No", isTwoPair("7H 2D 5S 6C 3D".split()))

assertEqual((5,2), isFullHouse("2H 2D 5S 5C 5D".split()))
assertEqual("No", isFullHouse("2H 3D 5S 5C 5D".split()))


assertEqual(7, isFlush("2H 3H 5H 4H 7H".split()))
assertEqual("No", isFlush("2H 3D 4H 5H 6H".split()))

assertEqual(6, isStraight("3D 2H 4H 5H 6H".split()))
assertEqual(7, isStraight("3D 7H 4H 5H 6H".split()))
assertEqual("No", isStraight("3D 7H 7H 5H 6H".split()))

assertEqual(6, isStraightFlush("3H 2H 4H 5H 6H".split()))
assertEqual("No", isStraightFlush("3D 2H 4H 5H 6H".split()))

assertEqual(14, isRoyalFlush("AH KH 10H QH JH".split()))
assertEqual("No", isRoyalFlush("AD KH 10H QH JH".split()))

assertEqual({"name": "Two of a Kind", "rank":2, "highcard":3}, identifyHand("3H 3D 5S 9C 2D".split()))
assertEqual({"name": "Two of a Kind", "rank":2, "highcard":5}, identifyHand("3H 5D 5S 9C 2D".split()))
assertEqual({"name": "Two Pair", "rank":3, "highcard": 5}, identifyHand("5H 5D 3S 3C 6C".split()))
assertEqual({"name": "Two Pair", "rank":3, "highcard": 6}, identifyHand("5H 6D 3S 3C 6C".split()))
assertEqual({"name": "Three of a Kind", "rank":4, "highcard":5}, identifyHand("5H 5D 5S 9C 2D".split()))
assertEqual({"name": "Straight", "rank":5, "highcard": 6}, identifyHand("3D 2H 4H 5H 6H".split()))
assertEqual({"name": "Flush", "rank":6, "highcard": 10}, identifyHand("10H 2H 3H 4H 5H".split()))
assertEqual({"name": "Full House", "rank":7, "highcard": 10}, identifyHand("10H 10H 10H 4C 4H".split()))
assertEqual({"name": "Four of a Kind", "rank":8, "highcard": 5}, identifyHand("5H 5D 5S 9C 5C".split()))
assertEqual({"name": "Straight Flush", "rank":9, "highcard": 6}, identifyHand("5H 2H 3H 4H 6H".split()))
assertEqual({"name": "Straight Flush", "rank":9, "highcard": 7}, identifyHand("5H 7H 3H 4H 6H".split()))
assertEqual({"name": "Royal Flush", "rank":10, "highcard": 14}, identifyHand("AH KH 10H QH JH".split()))

assertEqual({"name": "High Card", "rank":1, "highcard": 14}, identifyHand("2H 3D 5S 9C AH".split()))
assertEqual({"name": "High Card", "rank":1, "highcard": 13}, identifyHand("2H 3D 5S 9C KH".split()))

assertEqual("Black Wins with Flush", gameWinner("2H 3D 5S 9C KH".split(), "2H 3H 5H 9H KH".split()))
assertEqual("White Wins with Flush", gameWinner("2H 3H 5H 9H KH".split(), "2H 3D 5S 9C KH".split()))
assertEqual("Black Wins with Flush", gameWinner("2H 3H 5H 9H KH".split(), "2H 3H 5H 9H AH".split()))

#print(hand)
printFailures()