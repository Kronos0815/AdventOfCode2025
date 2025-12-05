import os

val = 50
count = 0

with open("input.txt") as f:
    for line in f:
       
        inputNumber = int(line[1:])
        
        # reduce input number to < 100
        while inputNumber > 99:
            inputNumber = inputNumber -100
            
        # reduce number 
        if line[0] == "L":
            val = val - inputNumber
            
            # wrap around
            if val < 0: 
                val = val + 100      

        # increase number
        elif line[0] == "R":
            val = val + inputNumber
            
            # wrap around
            if val > 99:
                val = val - 100
        else:
            print("error")
        
        # check if we are at 0
        if val == 0:
            count = count + 1
            
print("Count:" + str(count))