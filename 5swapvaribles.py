# swap two varibles in this program

x = input("enter first varible: ")
y = input("enter first varible: ")

print(x,y)

temp = x
x= y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

x = 90
y = 10
x, y = y, x
print("x= " , x)
print("y= ", y )