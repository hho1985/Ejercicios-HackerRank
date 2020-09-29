s="1:05:45PM"

hora, minutos, segundos = s.split(":")

print (segundos[2:])

if segundos[2:] == "PM" and hora =='12':
    hora = "00"
if segundos[2:] == "PM" and hora !='12':
    hora = str(int(hora) +12)
if segundos [2:] == "AM" and hora == '12':
    hora = '00'
    

print (hora+":"+ minutos+":"+ segundos[0:2])