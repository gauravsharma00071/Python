# flattend a list
# using list comprehension

list = [[2,3],[1],[3,4,5]]
flat_list = [num for sublist in list for num in sublist]
print(flat_list)

# using nested for loop (non Pythonic way)
print("using nested for loop")
list = [[2,3],[1],[3,4,5]]
flat_list = []
for sublist in list:
    for num in sublist:
        flat_list.append(num)
print(flat_list)


# using sum()
print("using sum()")

list = [[2,3],[1],[3,4,5]]
flat_list = sum(list,[])
print(flat_list)

# using lambda and reduce
print("using lambda and reduce")
list = [[2,3],[1],[3,4,5]]
print(reduce(lambda x,y: x+y, list))


# using itertools package
print("using itertools package")

import itertools

G_list = [[2,3],[1],[3,4,5]]
flat_list = list(itertools.chain(*G_list))
print(flat_list)