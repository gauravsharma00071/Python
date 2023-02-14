# binary Activation function in deep learning

b1 = eval(input("Enter first number: "))
b2 = eval(input("Enter Second number: "))
print(b1,b2)
w1 = eval(input("Enter weight 1: "))
w2 = eval(input("Enter weight 2: "))
print(w1,w2)

binary = b1*w1+b2*w2

print("Binary Activation function.")

if(binary>=1):
    print("1")
else:
    print("0")




