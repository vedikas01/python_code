# Q18
# check if 2 strings are anagrams of each other
def check_anagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        anagram = True
    else:
        anagram = False

    if anagram:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")

str1 = input("Enter a string : ")
str2 = input("Enter another string : ")
check_anagram(str1,str2)