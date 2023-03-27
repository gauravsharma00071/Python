num = int(input("Enter the number: "))
order = len(str(num))
#  changed num varible into string and calculated the length
sum = 0
temp = num
# sum of cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number")