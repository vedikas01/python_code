# Q14
# read multiple lines until user enters a blank line
def multiple_lines():
    input1 = []
    while True:
        line = input()
        if line == "":
            break
        input1.append(line)

    print("Text entered : ")
    for line in input1:
        print(line)

print("Enter multiple lines of text : ")
multiple_lines()