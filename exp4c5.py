from armstrong import is_armstrong
def generate_armstrong_numbers(start,end):
    armstrong_numbers=[]
    for num in range(start,end+1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
start=int(input("enter the start of range:"))
end=int(input("enter the end of the range:"))
armstrong_numbers=generate_armstrong_numbers(start,end)
print(f"armstrong number between {start} and {end}:",armstrong_numbers)
