def breakingRecords(scores):

    maximo= scores[0]
    minimo= scores[0]
    maxcount=0
    mincount=0

    for i in scores:

        if i>maximo:
            maximo=i
            maxcount+=1

        if i<minimo:
            minimo=i
            mincount+=1
            
    return maxcount,mincount