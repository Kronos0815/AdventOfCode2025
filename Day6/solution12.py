inputFromFile = []

with open ("example.txt","r") as file:
    
    for line in file:

        # Wir durchlaufen die Zeile und teilen das input in 4er päckchen und scheiden den letzten ab -> Sowohl leereichen als auch \n
        input = []
        line = list(line.strip())
        
        for index in range(0,len(line)):
            
            if line[index] == " ":
                line[index] = "0"

            
        # input = list(filter(None, temp))
        inputFromFile.append(line)

    # Operationen holen: letztes listenlement von hinten durchlaufen und die Operationen in ne extra liste packen
    
    
     
     
print(inputFromFile)