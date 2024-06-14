# Q25
# copy the content of one text file to another
def copy_contents(file_1, file_2):
    with open(file_1, 'r')as src:
        contents = src.read()
    with open(file_2, 'w')as dest:
        dest.write(contents)
    print("Contents of {} have been copied to {}".format(file_1,file_2))

file_1 = "doc1.txt"
file_2 = "doc2.txt"
copy_contents(file_1,file_2)