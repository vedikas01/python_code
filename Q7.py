# Q7
# take a string as input and returns its length
def str_length(str1):
    print("The length of string '{}' is : ".format(str1),len(str1))

str1 = input("Enter a string : ")
str_length(str1)

# OR
# def str_length(str1):
#     count = 0
#     for i in str1:
#         count+=1
#     str1_len = count
#     print("The length of the string '{}' is :".format(str1),str1_len)

# str1 = input("Enter a string : ")
# str_length(str1)