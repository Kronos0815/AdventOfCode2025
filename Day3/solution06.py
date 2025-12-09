import os 

with open ("input.txt", "r") as file:
    
    output = 0
    
    for line in file:

        line = list(line.strip())
        line = list(map(int, line))
        length = len(line)
        print(line)
        
        # Neue Idee ich lauf durch die Liste und suche mir das max Element mit mind 11 Elementen Abstand zum Rand
        
        # Nächster Durchlauf: Max mit mind 10 Stellen bis zum rand ... usw
        
        out = []
        start = 0
        distance = 12
        
        while distance > 0:
            
            index = 0
            max_value = line[start]
            end = length - distance + 1 # Bro dieses + 1 hat mich meinen letzten Nerv gekostet 
            
            # Elemente im kritischen Bereich nach maximum + Index durchsuchen
            
            j = 0
            
            print("Bereich: " ,line[start:end]) 
            for number in line[start:end]:
                
                # finde max im kritischen Bereich
                if max_value < number:
                    max_value = number
                    index = j
                # print("j:",j)
                j+=1
            
              
            # print("max",max_value, "index",index, "start", start, "end", end)
            # Neuer start ab dem Index der max ist
            
            start = start + index+1
            
            # print("neuer start: " , start)
            
            # kritischer Bereich wird nach hinten eins kleiner da wir eine Stelle weniger suchen
            distance = distance - 1
            out.append(max_value)
            # print(out)

        print("\n")        
        print("out",out)
        
        temp="".join(list(map(str,out)))
        output = output + int(temp) 
   
print(output)