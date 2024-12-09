try:
    number=float(input("enter a number:"))
    if number>=0:
        print(f"the number is{number}")
    else:
        raise ValueError("the number is negative!")
except ValueError as e:
    print(f"error:{e}")
            
