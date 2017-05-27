#Steve's hw week 5/25
from helpers import assertEqual

#print 5%2 --so modulus works

def add(x,y):
    return (x+y)

def mult(x,y):
    return (x*y)

def mod(x,y):
    return (x%y)
    
def crazyFunc(a,b):
    return "The sum is " + str(a+b)
    
def crazyFunc2(x,y):
    return "The addition is " + str(x+y)
    
def crazyFunc3(a,b,c):
    return "The " + a + " is " + str(b+c)
    
# http://codingdojo.org/kata/PokerHands/

assertEqual(8, add(4,4))
assertEqual(10, mult(2,5))
assertEqual(2, mod(10,4))
assertEqual("The sum is 5", crazyFunc(2,3))
assertEqual("The addition is 7", crazyFunc2(4,3))
assertEqual("The addition is 7", crazyFunc3("addition", 4, 3))

