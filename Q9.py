# Q9
# check if a substring is present in a string
def is_substring(ostring, sstring):
    o = len(ostring)
    s = len(sstring)
    for i in range(o-s+1):
        present = True
        for j in range(s):
            if(ostring[i+j]!=sstring[j]):
                present = False
                break

        if present:
            print("'{}' is present in original string".format(sstring))
            break
    else:
        print("'{}' is not present in original string".format(sstring))

ostring  = input("Enter a string : ")
sstring = input("Enter a sub string : ")
is_substring(ostring, sstring)