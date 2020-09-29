def divisibleSumPairs(n, k, ar):
    sum=0
    count=0

    for i in ar:
        count+=1
        for j in ar[count:]:
            if (i+j)%k==0:
                sum+=1

    return sum   