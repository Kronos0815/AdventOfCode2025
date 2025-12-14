freshIDs = []
testIDs = []
testedIDsFresh = []
countFreshIDs = 0

print("\n")
print("----------------------")

with open ("input.txt", "r") as file:
    
    switch = False
    
    for line in file:
        
        if line == "\n":
            switch = True
            continue
        
        if switch:
            testIDs.append(line.strip())
        else:
            freshIDs.append(line.strip().split("-"))
               
print("fresh: ",freshIDs)
print("test: ",testIDs)
print("----------------------")
print("\n")

for idToTest in testIDs:
    
    for area in freshIDs:
        
        if int(idToTest) >= int(area[0]) and int(idToTest) <= int(area[1]) and idToTest not in testedIDsFresh:
                print("area",area)
                print("approved:",idToTest)
                testedIDsFresh.append(idToTest)

print(testedIDsFresh)
print(len(testedIDsFresh))

# irgendwie bisschen zu einfach für Tag 5 oder?