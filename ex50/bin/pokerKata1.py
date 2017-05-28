from helpers import assertEqual, printFailures

#Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH

def face(x):
    firstCharacter = x[0]
    secondCharacter = x[1]
    if firstCharacter == "A":
        return 14
    if firstCharacter == "K": 
        return 13
    if firstCharacter == "Q":
        return 12
    if firstCharacter == "J":
        return 11
    if secondCharacter == "0":
        return 10
    if firstCharacter == "1":
        return 1
    else:
        return int(firstCharacter)
    


assertEqual(2, face("2H"))
assertEqual(3, face("3D"))
assertEqual(13, face("KD"))
assertEqual(12, face("QD"))
assertEqual(14, face("AH"))
assertEqual(11, face("JH"))
assertEqual(10, face("10H"))
assertEqual(1, face("1H"))


def suit(x):
   firstCharacter = x[0]
   if firstCharacter == "1":
       return x[2]
   else: return x[1]

assertEqual("H", suit("2H"))
assertEqual("D", suit("10D"))

printFailures()