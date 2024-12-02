def is_leap_year(year):
    return(year % 4==0 and year %100!= 0)or (year %400==0)
current_year=int(input("enter the current year:"))
final_year=int(input("enter the final year:"))
if final_year<=current_year:
    print("the final year must be greater than the current year.")
else:
    print(f"leap years from {current_year} to {final_year}:")
    for year in range(current_year,final_year+1):
        if is_leap_year(year):
            print(year)
