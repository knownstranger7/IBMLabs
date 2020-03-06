row = int(input())
col= int(input())
matrix1=[]
matrix2=[]
newmat=[]
for x in range(col):
    d=[]
    for y in range(row):
        d.append(int(input()))
    matrix1.append(d)
for x in range(col):
    d=[]

    for y in range(row):
        d.append(int(input()))
    matrix2.append(d)
for x in range(col):
    d=[]
    for y in range(row):
        d.append(matrix1[x][y]+matrix2[x][y])
    newmat.append(d)

print(newmat)