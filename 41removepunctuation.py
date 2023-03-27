punctuations = ''' !()[]{}-_+=<>,.?/::;"@#$% '''

string = input("Enter any string using punctuations: ")
no_punct = ""
for char in string:
    if char not in punctuations:
        no_punct = no_punct + char

print(no_punct)