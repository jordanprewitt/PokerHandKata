#Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH

def highCard(hand):
    # how to do with dictionary?
    hand.sort(reverse=True, key=face)
    firstCard = hand[0]
    return firstCard

def highCardWinner(black, white):
    blackHighCard = highCard(black)
    whiteHighCard = highCard(white)
    if face(blackHighCard) > face(whiteHighCard):
        return "Black Wins: " + blackHighCard
    else:
        return "White Wins: " + whiteHighCard

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

#10 card
def suit(x):
   firstCharacter = x[0]
   if firstCharacter == "1":
       return x[2]
   else: return x[1]
   
def rank(x,y):
    if (face(x) > face(y)) :
        return x
    else: return y

def isTwoOfAKind(hand):
    cardCounts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for card in hand:
        faceValue = face(card)
        countOfThisCardFace = cardCounts[faceValue]
        cardCounts[faceValue] = countOfThisCardFace + 1
        countOfThisCardFace = cardCounts[faceValue]
        if countOfThisCardFace == 2:
            return faceValue

    
    