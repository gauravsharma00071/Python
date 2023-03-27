num = int(input("Enter natural numbers count value: "))

if num < 0:
    print("enter a positive number.")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum Is ", sum)

# this problem can be solved using n*(n-1)/2
