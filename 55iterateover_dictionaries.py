#access both key and value using items()

dt = {'a':'juice','b':'grill','c':'corn','d':'gaurav'}
for key,value in dt.items():
    print(key,value)

# access both key and value without using items
print("key without using items")

print(key,dt[key])

# access both key and value using iteritems()

dt = {'a':'juice','b':'grill','c':'corn','d':'gaurav'}
for key, value in dt.iteritems():
    print(key,value)