kilometers = float(input("Enter the value in kilometer: "))
conv_fac = 0.641371
miles = kilometers * conv_fac
print("Kilometers is equal to :", miles)

miles = float(input("enter the value in miles: "))
kilometers = miles/conv_fac
print('%0.2f miles is equal to %0.2f miles' %(miles,kilometers))