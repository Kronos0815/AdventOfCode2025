
def shrink(listToshrink):
    
    input = listToshrink
    input.sort()
    print("sorted",input)
    while True:
    
        delete = 0
        for index in range(0,len(input)):
            
            if index < len(input)-1:
                currentStart = input[index][0]
                currentEnd = input[index][1]
                
                nextStart = input[index+1][0]
                nextEnd = input[index+1][1]
            else: 
                break
            
            if currentEnd >= nextStart and currentEnd >= nextEnd:
                input[index+1]=[0,0]
                delete = delete + 1             
            elif currentEnd >= nextStart and nextStart >= currentStart:
                input[index][1] = input[index+1][1]
                input[index+1]=[0,0]
                delete = delete + 1
                # print(delete)
        
        print(input)   
        if delete == 0:
            break 
            
        input.sort()
        # print(input,delete)
        input = input[delete:]   
        # print("cutted",input) 
        # print("\n")
        
        
    
    return input
    
    
    
    
    
    
    
    
    
    
    
    ## Alte Shrink Funktion 
    
    # input = listToshrink

    # freshIDs = []
    # freshIDs.append(input[0])

    # for area in input:
        
    #     # neuer Bereich
    #     start = int(area[0])
    #     end = int(area[1])
    
    #     # checken of neuer bereich sich mit bisherigen bereichen überschneidet:
    #     found = False
    #     for areaCovered in freshIDs:
            
    #         oldStart = int(areaCovered[0])
    #         oldEnd = int(areaCovered[1])
            
    #         if end >= oldStart and end <= oldEnd:
    #             areaCovered[0] = area[0]
    #             found = True
    #             break
    #         elif start <= oldEnd and start >= oldStart:
    #             areaCovered[1] = area[1]
    #             found = True
    #             break
    #         elif start <= oldStart and end >= oldEnd:
    #             areaCovered[0] = area[0]
    #             areaCovered[1] = area[1]
    #             found = True
    #             break
    #         elif start >= oldStart and end <= oldEnd:
    #             found = True
    #             break
            
    #     if not found :
    #         freshIDs.append(area)
    # return freshIDs


print("\n")
print("----------------------")

with open ("input.txt", "r") as file:
    
    inputFromFile = []
    
    for line in file:
        
        temp = []
        if line == "\n":
            break
        temp.append(line.strip().split("-"))
        
        for element in temp:
            integerElement = []
            integerElement.append(int(element[0]))
            integerElement.append(int(element[1]))
            inputFromFile.append(integerElement)

print(inputFromFile)
print("----------------------")
print("\n")

shrinkedIDs = shrink(inputFromFile)
print(shrinkedIDs)

result = 0
for id in shrinkedIDs:
    
    diff = id[1] - id[0] + 1
    result+=diff

print(result)
