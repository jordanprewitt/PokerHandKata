import sys

failuremessages = []

def assertEqual(expected, actual):
    if(expected != actual):
        sys.stdout.write('F')
        failuremessages.append("Expected: " + str(expected) + " but found: " + str(actual))
    else:
        sys.stdout.write('.')

def printFailures():
    if failuremessages == []:
        print "\n\nTests Succeeded"
    else:
        print "\n\nTests Failed!"
        for failure in failuremessages:
            print failure