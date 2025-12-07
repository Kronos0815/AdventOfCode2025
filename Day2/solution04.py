import os
import textwrap

with open ("input.txt" , "r") as file:
    
    input = file.readline().split(",")
    # print(input)
    output = 0
    
    for candidate in input:
        
        # print(candidate)
        temp = candidate.split("-")
        start = int(temp[0])
        end = int(temp[1]) + 1
        # print(temp, start, end)
        
        
        for number in range(start, end):
            
            number = str(number)
            lengthNumber = len(number)
            # print("Zahl: ", number)
            # print("Length: ", lengthNumber)
            
                        
            # Teiler raussuchen mit Modulo (2222 ergibt für i: 4,3,2 -> 4,2), von hinten nach vorne, für den Fall das Zahl 2222, wird nur 2 2 2 2 und nicht auch 22 22 gezählt -> dafür sorgt das break
            for i in range(lengthNumber+1,1,-1):
                
                if (lengthNumber % i == 0):
                    # print("Teiler: ", i)
                    
                    blub = False        
                    # print(splittedCandidate)
                    
                    # In i Teile Splitten
                    splittedCandidate = textwrap.wrap(number, int(lengthNumber/i))          
                    # https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts

                    # Checken ob alle Teile gleich sind
                    blub = len(splittedCandidate) == splittedCandidate.count(splittedCandidate[0]) 
                    # https://www.blog.pythonlibrary.org/2018/05/09/determining-if-all-elements-in-a-list-are-the-same-in-python/
                    
                    
                    if blub:
                        # Sobald ein Teiler bei der Zahl gleiche splits erzeigt zum Output addieren und Schleife breaken
                        output += int(number)
                        break
# Summe
print(output) 

