# Q19
# remove all punctuations from a given string
import string
str10 = input("Enter a string : ")
new_str = ""
for char in str10:
    if char not in string.punctuation:
        new_str+=char
print("After removing punctuation :",new_str)