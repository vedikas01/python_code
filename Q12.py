# Q12
# print the sum of the digits of a given number
def sum_of_digits(num):
    sum = 0
    while num!=0:
        sum = sum+int(num%10)
        num = int(num/10)
    print("The sum of the digits of the given number is :",sum)

num = int(input("Enter a number : "))
sum_of_digits(num)