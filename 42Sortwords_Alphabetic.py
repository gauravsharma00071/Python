string = input("Enter a string : ")
words = [word.lower() for word in string.split()]

# sort the list
words.sort()

print("The sorted words are: ")
for word in words:
    print(word)