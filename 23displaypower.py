#display powers of 2 using anonymous function

terms = 16

result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are: ", terms)
for i in range(terms):
    print("2 raise to power" , i, " is", result[i])