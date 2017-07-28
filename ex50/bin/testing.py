#Playing around
from helpers import assertEqual, failuremessages

list = (1,2,3)
print list

heroes = ["batman", "superman", "wonder woman"]

print heroes
print heroes[0]

heroes.append("green lantern")
print heroes
secretIdentities = ["bruce wayne", "clark kent", "diana prince", "hal jordan"]
print secretIdentities



rolodex = {}

rolodex = dict(zip(heroes, secretIdentities))

#for i in range(len(heroes)):
#    rolodex[heroes[i]] = secretIdentities[i]

print rolodex

print "hal jordan"
    
print 1>2


print "hey"


#https://developmentality.wordpress.com/2012/03/30/three-ways-of-creating-dictionaries-in-python/

#twister = [5, "how much wood could a wood chuck chuck if a wood chuck could chuck wood".split()]

#def tryingthis(word, index):
#    return word
#    print word

#tryingthis(6, 5)


#wordCounts = [0]*7

#def repeatWord(word, wordCounts):
#    for word in twister:
#        twister.index[1]
#        faceValue = faceValue + 1
#    return faceValue
#    print twister[0]
#repeatWord(5,"wood")

#def word(x):
 #   options = [0]*7
    
#print failuremessages