# Q24
# perform operations of a simple calculator
def calculator(num_1, num_2,op):
    if (op=='+'):
        print("Sum of {} and {} is :".format(num_1,num_2),num_1+num_2)
    elif (op=='-'):
        print("Difference of {} and {} is :".format(num_1,num_2),num_1-num_2)
    elif (op=='*'):
        print("Product of {} and {} is :".format(num_1,num_2),num_1*num_2)
    elif (op=='/'):
        print("Division of {} and {} is :".format(num_1,num_2),num_1/num_2)

num_1 = float(input("Enter num1 : "))
num_2 = float(input("Enter num2 : "))
op = input("Select the desired operator('+', '-', '*', '/'): ")
calculator(num_1,num_2,op)