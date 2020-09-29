def migratoryBirds(arr):
    B=[0,0,0,0,0,0]

    for i in arr:
        B[i]+=1

    return B.index(max(B))