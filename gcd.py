def find_gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
gcd=find_gcd(num1,num2)
print(f"the gcd of {num1} and {num2} is:{gcd}")
