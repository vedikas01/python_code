# Q17
# convert a given string to title case
def convert_titlecase(string):
    final_str = ""
    is_capital = True
    for char in string:
        if is_capital and char.isalpha():
            final_str+=char.upper()
            is_capital = False
        else:
            final_str+=char.lower()
        if char == " ":
            is_capital = True
    print("The given string in title case is :",final_str)

string = input("Enter any string : ")
convert_titlecase(string)