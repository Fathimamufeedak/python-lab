def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def sum_series(n):
    total_sum=0
    for i in range(1,n+1):
        term=(i**i)/factorial(i)
        total_sum+=term
    return total_sum
n=int(input("enter the number of terms:"))
result=sum_series(n)
print("the sum of the series up to",n,"terms is :",result)

