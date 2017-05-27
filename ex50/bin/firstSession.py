# Test Helper
# Make rest of arithmatic functions
# also make modulus 

from helpers import assertEqual

def add(x, y):
    return (x + y)
    
def mult(x, y):
    return x * y
    
def hello(name):
    return "Hi " + name
    
def bye(name):
    return "Bye " +name

def crazyFunc(a, b, c):
    return "The " + str(a) + " is " + str(b+c)

# Tests
assertEqual(6, add(2,4))
assertEqual(7, add(2,5))
assertEqual(6, mult(2,3))
assertEqual(4, mult(2,2))
assertEqual("Hi Jordan", hello("Jordan"))
assertEqual("Bye Steve", bye("Steve"))
assertEqual("The sum is 5", crazyFunc("sum", 2, 3))
assertEqual("The addition is 7", crazyFunc("addition", 4, 3))

