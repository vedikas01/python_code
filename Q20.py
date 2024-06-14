# Q20
# take a list of numbers and print their sum
lst = []
total = 0
n = int(input("Enter the size of list : "))
print("Enter the elements :-")
for i in range(0,n):
    elements = int(input())
    lst.append(elements)
    total+=lst[i]
    i+=1

print("The sum of the elements in the list is :",total)