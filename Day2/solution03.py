import os
import math
with open ("example.txt" , "r") as file:
    
    input = file.readline().split(",")
    #print(input)
    output = 0
    
    for candidate in input:
        
        #print(candidate)
        temp = candidate.split("-")
        start = int(temp[0])
        end = int(temp[1]) + 1
        print(temp, start, end)
        
        
        for number in range(start, end):
            number = str(number)
            blub = True
            lengthNumber = len(number)
            # print("Length: ", lengthNumber)
            if (lengthNumber % 2 == 0):
                j = 0
                while j < lengthNumber/2:
                    # print("j",number[j])
                    # print("j2",number[j + int(lengthNumber/2)])
                    if (number[j] == number[j + int(lengthNumber/2)]):
                        j += 1
                        # print(blub)
                    else: 
                        
                        blub = False
                        break   
                if blub:
                    # print("FalseID: " + number)
                    output = output + int(number)
        
        
    print(output)      

                    
        
        