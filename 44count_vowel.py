vowels = 'aeiou'

string = input("Enter any string : ")

# using caseless comparsion

string = string.casefold()
# dictionary of each vowel
count = {}.fromkeys(vowels, 0)

for char in string:     #count the vowel
    if char in count:
        count[char] += 1

print(count)

print("this is all about list and dictionry string")
# using a list and dictionary

string = 'hello it is program of couting vowels in any string'
string = string.casefold()
count = {x:sum([1 for char in string if char == x]) for x in 'aeiou'}
print(count)