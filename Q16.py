# Q16
# count the frequency of each character in a string
def count_freq(string):
    freq_count = {}
    for i in string:
        if i in freq_count:
            freq_count[i]+=1
        else:
            freq_count[i]=1
    print("The frequencies of each character in the string {} is :".format(string),freq_count)

string = input("Enter a string : ")
count_freq(string)