import os 

with open ("input.txt", "r") as file:
    
    output = 0
    
    for line in file:

        line = list(line.strip())
        line = list(map(int, line))
        print(line)
        length = len(line)
        
        cominations = []
        i=0
        while i < length:
            j=i+1
            while j < length:
                temp = ""
                a = str(line[i])
                b = str(line[j])
                temp = int(temp + a + b)
                cominations.append(temp)
                
                j += 1
            i += 1
        output = output + max(cominations)
                
print(output)