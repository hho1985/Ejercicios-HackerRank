ar= [ [11,2,4],[4,5,6], [10,8,-12]  ]
diagsup=0
diaginf=0
rango = len(ar)


for i in range (0,rango):
    diagsup= diagsup + ar[i][i]
    diaginf= diaginf + ar[i][(len(ar)-1) -i]

print (abs(diagsup-diaginf))