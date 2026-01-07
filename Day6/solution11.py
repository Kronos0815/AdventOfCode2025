inputFromFile = []

with open ("input.txt","r") as file:
    
    for line in file:
        temp = line.strip().split(" ")
        input = list(filter(None, temp))
        inputFromFile.append(input)
     
     
print(inputFromFile)
   
output = 0
calculation = 0

# Index an dem wir uns befinden
for index in range(0,len(inputFromFile[0])): 
    
    operation = inputFromFile[len(inputFromFile)-1][index]
    
    print(operation)
    
    if operation == "*":
        calculation = 1
    else:
        calculation = 0
    #print(calculation)
    
    
    # Durchläuft die Listen und holt sich immer den aktuellen Wert am Index
    for i in range(0,len(inputFromFile)-1):
        
        value = int(inputFromFile[i][index])
        # switch case je nach operation
        print(value)
        match operation:
            
            case "+":
                calculation+=value
            case "*":
                calculation*=value
          
    output+=calculation
    print(calculation)
    print(output)
    print("\n")
    
    
print(inputFromFile)    
print(output)
    
        
        

