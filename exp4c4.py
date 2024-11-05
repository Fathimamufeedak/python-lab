def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def print_fibonacci_series(n):
    print("fibonacci series:")
    for i in range(n):
        print(fibonacci(i),end=" ")
n=int(input("enter the number of term:"))
if n <=0:
    print("please enter a positive integer.")
else:
    print_fibonacci_series(n)

