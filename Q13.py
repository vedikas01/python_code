# Q13
# calculate the age of a user on the basis of birth date
def calculate_birthdate(curr_date, curr_month,curr_year, birth_date, birth_month, birth_year):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(birth_date>curr_date):
        curr_month = curr_month-1
        curr_date = curr_date+month[birth_month-1]

    if(birth_month>curr_month):
        curr_year = curr_year-1
        curr_month = curr_month+12

    final_date = curr_date-birth_date
    final_month = curr_month-birth_month
    final_year = curr_year-birth_year
    print("The calculated age is :-")
    print("{} Years {} Months {} Days".format(final_year, final_month, final_date))

curr_date = int(input("Current_date (DD) : "))
curr_month = int(input("Current_month (MM) : "))
curr_year = int(input("Current_year (YYYY) : "))

birth_date = int(input("Birth_date (DD) : "))
birth_month = int(input("Birth_month (MM) : "))
birth_year = int(input("Birth_year (YYYY) : "))

calculate_birthdate(curr_date, curr_month,curr_year, birth_date, birth_month, birth_year)