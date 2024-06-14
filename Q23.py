# Q23
# convert celsius to farenheit and vice versa based on user input
def degC_to_degF(C):
    Fahrenheit = float(9/5*C + 32)
    print("{} deg C in deg F is : {}".format(C,Fahrenheit))

def degF_to_degC(F):
    Celsius = float((F-32)*5/9)
    print("{} deg F in deg C is : {}".format(F,Celsius))

C = float(input("Enter temp in deg celsius : "))
degC_to_degF(C)
F = float(input("Enter temp in deg fahrenheit : "))
degF_to_degC(F)