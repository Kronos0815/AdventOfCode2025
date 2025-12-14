
def shrink(listToshrink):
    
    input = listToshrink

    freshIDs = []
    freshIDs.append(input[0])

    for area in input:
        
        # neuer Bereich
        start = int(area[0])
        end = int(area[1])
    
        # checken of neuer bereich sich mit bisherigen bereichen überschneidet:
        found = False
        for areaCovered in freshIDs:
            
            oldStart = int(areaCovered[0])
            oldEnd = int(areaCovered[1])
            
            if end >= oldStart and end <= oldEnd:
                areaCovered[0] = area[0]
                found = True
                break
            elif start <= oldEnd and start >= oldStart:
                areaCovered[1] = area[1]
                found = True
                break
            elif start <= oldStart and end >= oldEnd:
                areaCovered[0] = area[0]
                areaCovered[1] = area[1]
                found = True
                break
            elif start >= oldStart and end <= oldEnd:
                found = True
                break
            
        if not found :
            freshIDs.append(area)
    return freshIDs


inputFromFile = []


print("\n")
print("----------------------")

with open ("example.txt", "r") as file:
    
    for line in file:
        
        if line == "\n":
            break
        inputFromFile.append(line.strip().split("-"))


print(inputFromFile)
print("----------------------")
print("\n")

# solange shrinken bis nicht weiter geshrinkt werden kann lul
x = inputFromFile
blub = True

while blub:
    y = shrink(x)
    
    if len(x) == len(y):
        blub = False 
    else:
        x = y
        
freshIds = x
print(freshIds)
print("\n")



# was tu ich hier das ist so schlechter code :(
amountOfFreshIds = 0    

for uff in freshIds:
    
    idsInUff = int(uff[1]) - int(uff[0])+1
    amountOfFreshIds+=idsInUff
    
print(amountOfFreshIds)



# brute force

""" for area in input:
    start = int(area[0])
    end = int(area[1])
    
    for i in range(start,end+1):
        if i not in freshIDs:
            freshIDs.append(i)

print(freshIDs)
print(len(freshIDs)) """