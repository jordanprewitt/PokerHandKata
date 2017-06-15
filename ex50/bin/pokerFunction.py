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
    else:
        return int(firstCharacter)

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
    return isOfAKind(hand,2)

def isThreeOfAKind(hand):
        return isOfAKind(hand,3)
    
def isFourOfAKind(hand):
    return isOfAKind(hand,4)
    
def isOfAKind(hand, desiredCount):
    cardCounts = [0]*15
    for card in hand:
        faceValue=face(card)
        cardCounts[faceValue] = cardCounts[faceValue] + 1
       
    for card in hand:
        faceValue=face(card)
        if cardCounts[faceValue]==desiredCount:
            return faceValue
    return "No"
    
def isTwoPair(hand):
    hand.sort(reverse=False, key=face)
    firstTwoOfAKind = isTwoOfAKind(hand)
    hand.sort(reverse=True, key=face)
    secondTwoOfAKind = isTwoOfAKind(hand)
    if (firstTwoOfAKind == secondTwoOfAKind):
        return "No"
    return (firstTwoOfAKind, secondTwoOfAKind)
    
def isFullHouse(hand):
    if isThreeOfAKind(hand) != "No" and isTwoOfAKind(hand) != "No":
         return (isThreeOfAKind(hand), isTwoOfAKind(hand))
    else:
        return "No"
    
def isFlush(hand):
    firstSuit = suit(hand[0])
    for card in hand:
        if(firstSuit != suit(card)):
            return "No"
    return face(highCard(hand))

def isStraight(hand):
    hand.sort(reverse=False, key=face)
    if (face(hand[4]) - face(hand[0])) == 4 and  isTwoOfAKind(hand) == "No" and  isThreeOfAKind(hand) == "No" and  isFourOfAKind(hand) == "No":
        return face(hand[4])
    else:
        return "No"
        
def isStraightFlush(hand):
    if isFlush(hand) != "No" and isStraight(hand) != "No":
        return isStraight(hand)
    else:
        return "No"
    

def isRoyalFlush(hand):
    wasStraightFlush = isStraightFlush(hand) 
    if wasStraightFlush != "No" and wasStraightFlush == 14:
        return 14
    else:
        return "No"
        
def identifyHand(hand):
    if isTwoPair(hand) !="No":
        highPair = isTwoPair(hand)[1]
        return {'name': "Two Pair", "rank": 3, "highcard": highPair}
    elif isFullHouse(hand) != "No":
        return {"name": "Full House", "rank": 7, "highcard": isFullHouse(hand)[0]}
    elif isTwoOfAKind(hand) != "No":
        return {'name': "Two of a Kind", "rank": 2, "highcard": isTwoOfAKind(hand)}
    elif isThreeOfAKind(hand) != "No":
        return {'name': "Three of a Kind", "rank": 4, "highcard": isThreeOfAKind(hand)}
    elif isRoyalFlush(hand) != "No":
        return {"name": "Royal Flush", "rank": 10, "highcard": 14}
    elif isStraightFlush(hand) != "No":
        return {"name": "Straight Flush", "rank": 9, "highcard": isStraightFlush(hand)}
    elif isStraight(hand) != "No":
        return {"name": "Straight", "rank": 5, "highcard": isStraight(hand)}
    elif isFlush(hand) != "No":
        return {"name": "Flush", "rank": 6, "highcard": isFlush(hand)}
    elif isFourOfAKind(hand) != "No":
        return {'name': "Four of a Kind", "rank": 8, "highcard": isFourOfAKind(hand)}
    else:
        return {"name": "High Card", "rank": 1, "highcard": face(highCard(hand))}
    
    
    
    