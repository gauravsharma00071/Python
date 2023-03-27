#access index of a list using for loop

# using enumerate

list = [2,3,4,5,6,6,7]

for index, val in enumerate(list):
    print(index,val)

print("indexing value from non zero value")

# start indexing using non zero value

for index, val in enumerate(list, start=1):
    print(index,val)

# without using enumerate()
print("without using enumerate function")
list = [3,4,5,6,7]
for index in range(len(list)):
    value = list[index]
    print(index,val)

