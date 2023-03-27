rows = int(input("enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print("\n")

    # print half pyramid using numbers
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end = " ")
    print("\n")

# print half pyramind using charachters

rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet,end=" ")
    ascii_value += 1
    print("\n")

# inverted half pyramid using * and numbers

rows = int(input("enter number of rows: "))

for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end="")
    print("\n")


# inverted half pyramid using numbers
rows = int(input("enter number of rows: "))

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")

# print full pyramid
k = 0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end= "  ")
    while k != (2*i-1):
        print("* ",end="")

    k = 0
    print()

# full pyramid of numbers
k = 0
count = 0
count1 = 0

for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(" ",end="")
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end = " ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1),end= " ")
        k += 1
    count1 = count = k = 0
    print()

