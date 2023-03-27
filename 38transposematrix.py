X = [[1,2,3],
     [3 , 5,6],
     [7,8,9]]
print(X)

result = [[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)