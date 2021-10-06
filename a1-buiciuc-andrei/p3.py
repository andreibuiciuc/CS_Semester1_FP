#
#  Implement the program to solve the problem statement from the third set here
#    Age of a person in days
#        
#     

class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def leap_year(x, y):
    #We consider a year to be a leap year if it is a multiple of 4 or 400, except being a multiple of 100
    
    value = 0
    for index in range(x.year, y.year + 1):
        if (index % 4 == 0 or index % 400 == 0) and index % 100 != 0:
            value = value + 1

    return value

def age_in_days(date_birth, date_current):

    days1 = 0
    days2 = 0

    #We add days from the years and also the days of the current month
    days1 = 365 * date_birth.year + date_birth.day
    days2 = 365 * date_current.year + date_current.day

    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #We add days from the months, not including the current one
    for index in range(0, date_birth.month - 1):
        days1 = days1 + month_list[index]
    
    for index in range(0, date_current.month - 1):
        days2 = days2 + month_list[index]

    #We add days for each leap year we found
    #days1 = days1 + leapYear(date_birth)
    #days2 = days2 + leapYear(date_current)

    age = days2 - days1
    age = age + leap_year(date_birth, date_current)
    return age


print("Introduce the date of birth: ")
a = int(input("Day: "))
b = int(input("Month: "))
c = int(input("Year: "))
print("Introduce the current date: ")
x = int(input("Day: "))
y = int(input("Month: "))
z = int(input("Year: "))

date1 = date(a, b, c)
date2 = date(x, y, z)

print(age_in_days(date1, date2))