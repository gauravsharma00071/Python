a1 = int(input("Enter the first number : "))
a2 = int(input("Enter the second number : "))
print(a1,a2)
w1 = 1
w2 = 1
# w1 = int(input("Enter the weight 1"))
# w2 = int(input("Enter the weight 2"))
# print(w1,w2)
th = 2
# th = int(input("Enter the threshold value"))
# print(th)

thr = a1*w1 + a2*w2
if(thr>=th):
    print(1)
else:
    print(0)
    
#if(thr<=th)            nand function 