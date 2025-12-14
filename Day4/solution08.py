import os


def checkCharForRemoval(above, current, bellow, index):
    
    adjCounter = 0 
    remove = False
    
    for k in range(index-1,index+2):
        if above[k] == "@" or above[k] == "#":
            adjCounter+=1
                
    if current[index-1] == "@" or current[index-1] == "#":
        adjCounter+=1
        
    if current[index+1] == "@" or current[index+1] == "#":
            adjCounter+=1
        
    for k in range(index-1,index+2):
        if bellow[k] == "@" or bellow[k] == "#":
            adjCounter+=1
        
    if adjCounter < 4:
        remove = True       
                    
    return remove
    
    
    
with open ("input.txt", "r") as file:
    
    # Idee: Ich nehme mir immer 3 Zeilen. Wenn ich die mittlere Zeile überprüfen will, muss ich zum Beispiel am Index 2 folgende Zeichen prüfen:
    
        # Zeile zuvor: Index 1,2,3
        # Aktuelle Zeile: Index 1,3
        # Nächste Zeile: Index 1,2,3
        
    # Irgendwie muss ich die Randfälle abdecken wenn keine Zeile davor oder danach exisitert, bzw. wenn ich an den Ränder ankomme
    
    docLength = -1
    lineLength = None 
    input = []
    
    print("\n")
    print("Rätsel:")
    for line in file:
        input.append("."+line.strip()+".")
        print("."+line.strip()+".")
        docLength += 1
        if lineLength == None:
            lineLength = len(line)+2
    
    prevLine = "."*lineLength
    # buffer at the end 
    input.append(prevLine)
    output = 0
    rollsLeft = True
    
    
    print("\n")
    print("--------------")
    
    while rollsLeft:

        prevLine = "."*lineLength
        
        # falsch weil nur temp objekt
        # for index, object in enumerate(input):
        
        for rowIndex in range(0,len(input)):
            
            object = input[rowIndex]
            
            # Randfall am Ende abfangen
            if rowIndex <= docLength:
                nextLine = input[rowIndex+1]
            else:
                nextLine = prevLine

            
            #print("pre",object)
            
            
            for index, char in enumerate(object):
                
                if char == "@":

                    if checkCharForRemoval(prevLine,object,nextLine,index):
                        object = object[:index] + "#" + object[index + 1:]
            input[rowIndex] = object
            
            print(object)    
                    
            prevLine = object 

        #print(input)
        counterDeletion = 0
        for row_index in range(len(input)):
            
            object = input[row_index]
            newObject = ""
            
            for char in object:
                
                if char == "#":
                    
                    newObject += "."
                    counterDeletion += 1
                else: 
                    newObject+=char

            input[row_index] = newObject
            
           
        print("Löschungen:",counterDeletion)
        print("\n") 
        
        output += counterDeletion
        
        if counterDeletion == 0:
            rollsLeft = False
            

print("Erreichbare Rollen",output)                    
                
                
                
                
                
                