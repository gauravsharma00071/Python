my_list = [ 23,45,5667,42,60,75,80]
result = list(filter(lambda x: (x % 5 == 0),my_list))
print("numbers divisible by 5 are: ", result)

