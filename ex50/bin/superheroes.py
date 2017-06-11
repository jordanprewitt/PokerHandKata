#Playing around
#from helpers import assertEqual, failuremessages

list = (1,2,3)


heroes = ["batman", "superman", "wonder woman"]
heroes.append("green lantern")

secretIdentities = ["bruce wayne", "clark kent", "diana prince", "hal jordan"]
homeTown = ["gotham", "krypton", "themiscyra", "space"]
rolodex = {}
#rolodex = dict(zip(heroes, secretIdentities))

for i in range(len(heroes)):
    hero = heroes[i]
    hero_info = {}
    
    hero_info["secret identity"] = secretIdentities[i]
    hero_info["home town"] = homeTown[i]
    rolodex[hero] = hero_info

print rolodex
print
print rolodex['batman']
print
print rolodex['batman']['home town']
