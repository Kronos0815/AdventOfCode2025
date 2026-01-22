inputFromFile = []
formatted = []
temp=""
output=0

# Funktion um die entsprechende Operation auf den Array anzuwenden
def calcArray(inputArray, operation):
    
    match operation:
        
        case "*":
            val = 1
            for i in inputArray:
                val*=i
            return val
        case "+":
            val = 0
            for i in inputArray:
                val+=i
            return val
        case _:
            return 0


with open ("input.txt","r") as file:
    
    for line in file:
        
        inputFromFile.append(line)
    
    # Durchlaufe die Tabelle von hinten nach vorne
    for j in range(len(inputFromFile[0])-2,-1,-1):
        
        #reset output
        #output = 0
        
        # Spalte von oben nach unten durchlaufen
        for i in range(0,len(inputFromFile)-1):
            
            # Betrachte Wert an der entsprechenden Stelle wenn ungleich "" fügen wir die Zahl der sich aufbauenden nummer hinzu
            x = inputFromFile[i][j]        
            
            if x != " ":
                temp+=x      
        
        # Wenn Spalte leer, dann wende die ensprechende Operation auf den bisherigen Array an
        if temp == "":  
            operation = inputFromFile[len(inputFromFile)-1][j+1]
            output += calcArray(formatted, operation) 
            print(formatted, operation, output, j)
            formatted = []
        
        # TW : Scheiße incoming
        elif j == 0:
            val = int(temp)
            formatted.append(val)
            operation = inputFromFile[len(inputFromFile)-1][j]
            output += calcArray(formatted, operation) 
            print(formatted, operation, output, j)
            formatted = []
        
        # Wenn Spalte nicht leer füge die Zahl dem Array hinzu
        else:
            val = int(temp)
            formatted.append(val)
        
        #reset temp    
        temp = "" 
    
print(output)        


