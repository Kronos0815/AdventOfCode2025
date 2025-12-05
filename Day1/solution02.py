import os

val = 50
count = 0

with open("input.txt") as f:
    for line in f:
        
        # Debug
        print(line) 
        inputNumber = int(line[1:])
        
        # repetitions over 100
        rep = 0
        
        # reduce input number to < 100
        while inputNumber > 99:
            # count 0 crossings
            rep = rep + 1
            inputNumber = inputNumber -100
            
        # reduce number    
        if line[0] == "L":
            
            # ugly as fuck but works
            if val == 0:
                rep = rep - 1 
                
            val = val - inputNumber
            
            if val < 0: 
                rep = rep + 1
                val = val + 100
                
            if val == 0:
                rep = rep +1    
                   
        # increase number
        elif line[0] == "R":
            
            val = val + inputNumber
            
            if val > 99:
                rep = rep + 1
                val = val - 100

        else:
            print("error")
        print("Value: " + str(val))
        
        # übergänge über 100
        count = count + rep
        print("zwischenCount:" + str(count))
            
            
print("Count:" + str(count))
