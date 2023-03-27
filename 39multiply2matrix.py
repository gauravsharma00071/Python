x = [[1,2,3], [4,5,6],[7,8,9]]
y = [[10,20,30,10],[20,40,50,60],[11,12,13,13]]

result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

for r in result:
    print(r)


# using nested comprehension

result = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]
for r in result:
    print(r)
