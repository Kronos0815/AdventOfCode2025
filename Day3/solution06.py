import os 

with open ("example.txt", "r") as file:
    
    output = 0
    
    for line in file:

        line = list(line.strip())
        line = list(map(int, line))
        length = len(line)
        
        
        # Neue Idee ich lauf durch die Liste und suche mir das max Element mit mind 11 Elementen Abstand zum Rand
        
        # Nächster Durchlauf: Max mit mind 10 Stellen bis zum rand ... usw
        
        out = []
        start = 0
        distance = 12
        
        while distance > 0:
            
            index = 0
            max_value = line[start]
            end = length - distance
            
            # Elemente im kritischen Bereich nach maximum + Index durchsuchen
            
            j = 0
            
            # print("Bereich: " ,line[start:end])  
            for number in line[start:end]:
                
                # finde max im kritischen Bereich
                if max_value < number:
                    max_value = number
                    index = j
                # print("j:",j)
                j+=1
                
                
            
              
            # print("max",max_value, "index",index, "start", start, "end", end)
            # Neuer start ab dem Index der max ist
            
            start = start + index + 1
            
            # print("neuer start: " , start)
            
            # kritischer Bereich wird nach hinten eins kleiner da wir eine Stelle weniger suchen
            distance = distance - 1
            out.append(max_value)
            # print(out)

        print("\n")        
        print("out",out)
        
        temp="".join(list(map(str,out)))
        output = output + int(temp) 
        
        
        
        
        # temp = [None] * length
        # out =[]
        # count = 0

        # print(temp)
        # for i in range(9,-1,-1):
            
        #     j = length-1
        #     while j >= 0 and count <12:
        #         element = line[j]
        #         if element == i:
        #             temp.insert(j,element)
        #             count+= 1
        #         j-=1
            
        # for k in temp:
        #     if k != None:
        #         out.append(k)
        
                
    
       
            
        # length = len(line)
        
        # for i in range(0,10):
        #     j = len(line) -1
            
        #     while j > -1:
                
        #         if len(line) > 12 and line[j] == i:
        #             line.pop(j)
                    
        #         j -=1
                
print(output)