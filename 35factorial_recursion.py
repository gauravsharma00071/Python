def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
num = 5
if num < 0:
    print("Enter a positive number:")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of given number",num, " is", recur_factorial(num))
