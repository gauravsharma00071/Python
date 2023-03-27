lower = int(input("Enter the value form we want to start print:"))
upper = int(input("Enter the largest value of prime numbers:"))
print(lower, upper)

print("Prime number between ",lower ,"and" , upper , "are: ")
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
            else:
                print(num)