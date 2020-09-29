    for i,j in zip(a,b):
        if i>j:
            Alice+=1
        if i<j:
            Bob+=1
        
    return Alice, Bob