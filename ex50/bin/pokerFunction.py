# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH

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
    else:
        return int(firstCharacter)

#issues below
def suit(card):
    firstCharacter = card[0]
    if firstCharacter == "1":
        return card[2]
    else: return card[1]
   
def highcard(hand):
    faceList = []
    for card in hand:
        faceList.append(face(card))
    faceList.sort()
    return faceList[4]
   
def ofAKind(a,b):
    if face(a) == face(b):
        return numberToString(face(a))
    else:
        return "no"

def cardCount(hand):
    list = [0]*15
    for card in hand:
        list[face(card)] = list[face(card)] + 1
    return list
    
def numberToString(cardFace):
    if cardFace == 14:
        return "A"
    if cardFace == 13: 
        return "K"
    if cardFace == 12:
        return "Q"
    if cardFace == 11:
        return "J"
    else:
        return str(cardFace)

def onePair(hand):
    counts = cardCount(hand)
    for faceValue in range(15):
        if counts[faceValue] == 2:
            return numberToString(faceValue)
    return "no"
        
    
    
    