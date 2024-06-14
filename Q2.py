# Q2
# check whether a given number is even or odd
def odd_even(num):
    if num%2==0:
        print("%d is even"%num)
    else:
        print("%d is odd"%num)
    
num = int(input("Enter a number : "))
odd_even(num)