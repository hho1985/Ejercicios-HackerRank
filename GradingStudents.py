def gradingStudents(grades):
    notas=[]

    for i in grades:
        if i<38 or i%5<3:
            notas.append(i)
        else:
            notas.append (i-(i%5) +5)

    return notas



grades =[30,91,44,99]

print(gradingStudents(grades))