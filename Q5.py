# Q5
# take a string input from the user and write it in a text file
user_input = input("Enter a string : ")
file_name = "doc1.txt"
with open(file_name , "w")as file:
    file.write(user_input)
print("The text has been written to {}".format(file_name))
