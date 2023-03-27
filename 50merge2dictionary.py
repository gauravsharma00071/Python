# using the | operator merge two dictionaries

dict1 = {1:'a', 2 : 'b'}
dict2 = {2: 'c', 4: 'd'}

print(dict1 | dict2)

# using ** operator merge two dictionary

print({**dict1, **dict2})

# using copy() and update()

dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)



