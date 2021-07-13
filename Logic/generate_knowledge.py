from field_var import field_var

def generate_knowledge(conf):
    kb = []
    
    # calculate # of vehicles active 
    
    num_active, num_stopped, num_right_of_ways = active_vehicles(conf)
    
    for i, con in enumerate(conf):
        if con == "empty":
            new_proposition = field_var(i, 0)
            kb.append(new_proposition)
            
        if con == "right of way":
            new_proposition = field_var(i, 1)
            kb.append(new_proposition)
            
        if con == "stop":
            new_proposition = field_var(i, num_active) 
            kb.append(new_proposition)
     
        if con == "":
            new_proposition = field_var(i, 9)
            kb.append(new_proposition)
    
    # STOP
    # 1 stop + one string
    if num_active == 2 and num_stopped == 1:
        if kb[0] == "V09": 
            kb[0] = "V01" 
        if kb[1] == "V19": 
            kb[1] = "V11" 
        if kb[2] == "V29": 
            kb[2] = "V21" 
        if kb[3] == "V39": 
            kb[3] = "V31" 
   
    
    # 3 empty cases  + one ""     
    if num_active == 1:
        new_proposition = field_var(0,9) + " & " + field_var(1,0) + " & " + field_var(2,0) + " & " + field_var(3,0) + " ==> " + field_var(0,1)
        kb.append(new_proposition)
        
        new_proposition = field_var(0,0) + " & " + field_var(1,9) + " & " + field_var(2,0) + " & " + field_var(3,0) + " ==> " + field_var(1,1)
        kb.append(new_proposition)
        
        new_proposition = field_var(0,0) + " & " + field_var(1,0) + " & " + field_var(2,9) + " & " + field_var(3,0) + " ==> " + field_var(2,1)
        kb.append(new_proposition)
        
        new_proposition = field_var(0,0) + " & " + field_var(1,0) + " & " + field_var(2,0) + " & " + field_var(3,9) + " ==> " + field_var(3,1)
        kb.append(new_proposition)
    
    # CASE 1 RIGHT WAY
    if num_right_of_ways == 1:
         
        # right of way + stop + string + empty    
        if num_stopped == 1 and num_active == 3:
            if kb[0] == "V09": 
                kb[0] = "V02" 
            if kb[1] == "V19": 
                kb[1] = "V12" 
            if kb[2] == "V29": 
                kb[2] = "V22" 
            if kb[3] == "V39": 
                kb[3] = "V32" 
                
        # 1.1 right of way + 1 string + 2 empty
        if num_stopped == 0 and num_active == 2:
            if kb[0] == "V09": 
                kb[0] = "V02" 
            if kb[1] == "V19": 
                kb[1] = "V12" 
            if kb[2] == "V29": 
                kb[2] = "V22" 
            if kb[3] == "V39": 
                kb[3] = "V32" 
        
         # 0 - 1 - 2
        new_proposition = field_var(0,9) + " & " + field_var(1,9) + " & " + field_var(2,9) + " ==> " + field_var(0,4) + " & " + field_var(1,3) + " & " + field_var(2,2)
        kb.append(new_proposition)
        
        # 1 - 2 - 3
        new_proposition = field_var(1,9) + " & " + field_var(2,9) + " & " + field_var(3,9) + " ==> " + field_var(1,4) + " & " + field_var(2,3) + " & " + field_var(3,2)
        kb.append(new_proposition)
        
        # 2 - 3 - 0
        new_proposition = field_var(2,9) + " & " + field_var(3,9) + " & " + field_var(0,9) + " ==> " + field_var(2,4) + " & " + field_var(3,3) + " & " + field_var(0,2)
        kb.append(new_proposition)
        
        # 3 - 0 - 1
        new_proposition = field_var(3,9) + " & " + field_var(0,9) + " & " + field_var(1,9) + " ==> " + field_var(3,4) + " & " + field_var(0,3) + " & " + field_var(1,2)
        kb.append(new_proposition)
  
        # 0 - 1
        new_proposition = field_var(0,9) + " & " + field_var(1,9) + " ==> " + field_var(0,3) + " & " + field_var(1,2)
        kb.append(new_proposition)
        
        # 1 - 2
        new_proposition = field_var(1,9) + " & " + field_var(2,9) + " ==> " + field_var(1,3) + " & " + field_var(2,2)
        kb.append(new_proposition)
        
        # 2 - 3
        new_proposition = field_var(2,9) + " & " + field_var(3,9) + " ==> " + field_var(3,2) + " & " + field_var(2,3)
        kb.append(new_proposition)
        
        # 3 - 0
        new_proposition = field_var(3,9) + " & " + field_var(0,9) + " ==> " + field_var(3,3) + " & " + field_var(0,2)
        kb.append(new_proposition)
        
       
    
    else:
        
        # 0 - 1 - 2
        new_proposition = field_var(0,9) + " & " + field_var(1,9) + " & " + field_var(2,9) + " ==> " + field_var(0,3) + " & " + field_var(1,2) + " & " + field_var(2,1)
        kb.append(new_proposition)
        
        # 1 - 2 - 3
        new_proposition = field_var(1,9) + " & " + field_var(2,9) + " & " + field_var(3,9) + " ==> " + field_var(1,3) + " & " + field_var(2,2) + " & " + field_var(3,1)
        kb.append(new_proposition)
        
        # 2 - 3 - 0
        new_proposition = field_var(2,9) + " & " + field_var(3,9) + " & " + field_var(0,9) + " ==> " + field_var(2,3) + " & " + field_var(3,2) + " & " + field_var(0,1)
        kb.append(new_proposition)
        
        # 3 - 0 - 1
        new_proposition = field_var(3,9) + " & " + field_var(0,9) + " & " + field_var(1,9) + " ==> " + field_var(3,3) + " & " + field_var(0,2) + " & " + field_var(1,1)
        kb.append(new_proposition)
        
        # 0 - 1
        new_proposition = field_var(0,9) + " & " + field_var(1,9) + " ==> " + field_var(0,2) + " & " + field_var(1,1)
        kb.append(new_proposition)
        
        # 1 - 2
        new_proposition = field_var(1,9) + " & " + field_var(2,9) + " ==> " + field_var(1,2) + " & " + field_var(2,1)
        kb.append(new_proposition)
        
        # 2 - 3
        new_proposition = field_var(2,9) + " & " + field_var(3,9) + " ==> " + field_var(2,2) + " & " + field_var(3,1)
        kb.append(new_proposition)
        
        # 3 - 0
        new_proposition = field_var(3,9) + " & " + field_var(0,9) + " ==> " + field_var(3,2) + " & " + field_var(0,1)
        kb.append(new_proposition)
        
        
               
    return kb
                                        
def active_vehicles(conf):
    empty = 0
    stopped = 0
    right_of_ways = 0
    
    for con in conf:
        if con == "empty":
            empty += 1   
        if con == "stop":
            stopped += 1
        if con == "right of way":
            right_of_ways += 1
            
    return len(conf) - empty, stopped, right_of_ways
