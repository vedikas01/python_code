# Q6
# read the contents of a text file and print it in console
file_nm = "doc1.txt"
with open(file_nm, "r")as file:
    content = file.read()
    print("The content of the file is :",content)