import calendar
def is_leap_year(year):
    return calendar.isleap(year)
year=int(input("enter a year:"))
if is_leap_year(year):
    print(f"{year}is a leap year")
else:
    print(f"{year}is not a leap year")
