def is_even(number):
    return number % 2==0
def main():
    number=int(input("enter a number:"))
    if is_even(number):
        print(f"{number}is even")
    else:
        print(f"{number}is odd:")
main()

