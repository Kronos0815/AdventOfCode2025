import os

with open ("input.txt", "r") as file:
    
    # Idee: Ich nehme mir immer 3 Zeilen. Wenn ich die mittlere Zeile überprüfen will, muss ich zum Beispiel am Index 2 folgende Zeichen prüfen:
    
        # Zeile zuvor: Index 1,2,3
        # Aktuelle Zeile: Index 1,3
        # Nächste Zeile: Index 1,2,3
        
    # Irgendwie muss ich die Randfälle abdecken wenn keine Zeile davor oder danach exisitert, bzw. wenn ich an den Ränder ankomme
    
    docLength = -1
    lineLength = None 
    input = []
    
    # Print test:
    print("Testbild")
    
    for line in file:
        input.append("."+line.strip()+".")
        print("."+line.strip()+".")
        docLength += 1
        if lineLength == None:
            lineLength = len(line)+2
    
    
    prevLine = "."*lineLength
    input.append(prevLine)
    output = 0
    
    print("\n")
    
    for index, object in enumerate(input):
        
        # Randfall am Ende abfangen
        if index <= docLength:
            nextLine = input[index+1]
        else:
            nextLine = prevLine
    
        print(object)
        for index, char in enumerate(object):
        
            #print(index)
            adjCounter = 0 
            
            if char == "@":

                # brute force:
                
                for k in range(index-1,index+2):
                    if prevLine[k] == "@":
                        adjCounter+=1
                        
                if object[index-1] == "@":
                    adjCounter+=1
                    
                if object[index+1] == "@":
                    adjCounter+=1
                
                for k in range(index-1,index+2):
                    if nextLine[k] == "@":
                        adjCounter+=1
                
                if adjCounter < 4:
                    output += 1
                    print(output)         
                     
        prevLine = object        
                  
print(output)
                    
                
                
                
                
                
                