# Q11
# generate first n numbers in fibonacci series
def fibonacci_seq(num,fib):
    if num<=0:
        print("Invalid")
    elif num==1:
        print("[0]")
    elif num==2:
        print("[0,1]")
    else:
        for i in range(2,num):
            new_no = fib[i-1]+fib[i-2]
            fib.append(new_no)
            i+=1
        print(fib)

num = int(input("Enter any number : "))
fib = [0,1]
fibonacci_seq(num,fib)