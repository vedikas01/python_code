# Q22
# return the minimum and maximum values in a list of numbers
lst2 = []
len_ls2 = int(input("Enter the size of the list : "))
print("Enter the elements in the list :-")
for i in range(0,len_ls2):
    ele = int(input())
    lst2.append(ele)
max = lst2[0]
min = lst2[0]

for i in lst2:
    if i>max:
        max=i
    elif i<min:
        min=i

print("Max : {}, min : {}".format(max,min))