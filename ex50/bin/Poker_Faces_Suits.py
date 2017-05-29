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

def suit(x):
   firstCharacter = x[0]
   if firstCharacter == "1":
       return x[2]
   else: return x[1]