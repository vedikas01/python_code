# Q21
# count the occurence of a specific element in the list
lst1 = []
m = int(input("Enter the size of the list : "))
print("Enter the elements :-")
for i in range(0,m):
    elem=input()
    lst1.append(elem)
    
p = input("Enter the element to find its occurences : ")
count = 0
for i in lst1:
    if i==p:
        count+=1

if count<=0:
    print("Element is not present in the list")
else:
    print("The occurence of {} in the list is :".format(p),count)
