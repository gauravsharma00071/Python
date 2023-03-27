my_string = input("Enter a string: ")

# make it suitable for caseless comparision
my_string = my_string.casefold()

rev_string = reversed(my_string)
# check it it equal to both side

if list(my_string) == list(rev_string):
    print("The string is a palindrome")
else:
    print("The String is not a palindrome")