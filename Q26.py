# Q26
# check if a given string starts with a prefix or end with a suffix
def is_prefix(string,prefix):
    if(len(prefix)>len(string)):
        return False
    for i in range(0,len(prefix)-1):
        if(string[i]!=prefix[i]):
            return False        
    return True

def is_suffix(string,suffix):
    if(len(suffix)>len(string)):
        return False
    for i in range(1,len(suffix)+1):
        if(string[-i]!=suffix[-i]):
            return False    
    return True   

string = input("Enter a string : ")
prefix = input("Enter prefix : ")
suffix = input("Enter suffix : ")

if is_prefix(string,prefix)==True:
    print("The string contains the prefix '{}'".format(prefix))
else:
    print("The string does not contain the prefix")

if is_suffix(string,suffix)==True:
    print("The string consists of suffix '{}'".format(suffix))
else:
    print("The string does not consists of suffix")