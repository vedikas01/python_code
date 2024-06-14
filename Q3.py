# Q3
# calculate the factorial of a user input number
def factorial(num):
    if num==0:
        print("Factorial of 0 is 1")
    elif num<0:
        print("Error!")
    else:
        i=1
        fact=1
        while i<=num:
            fact=fact*i
            i+=1
        print("Factorial of %d is :"%(num),fact)

num = int(input("Enter a num : "))
factorial(num)