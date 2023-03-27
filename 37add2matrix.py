X = [[1,2,4],
     [4,6,7],
     [8,9,2]]
print(X)
Y = [[5,6,7],
     [4,6,7],
    [9,10,2]]
print(Y)
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
        print(r)


# adding using nested list
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)