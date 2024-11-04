def compare(s1,s2,n):
    return s1[:n]==s2[:n]
s1=input("enter the first string:")
s2=input("enter the second string:")
n=int(input("enter the number of character to compare(n):"))
if compare(s1,s2,n):
    print("true-the first ",n,"characters are same")
else:
    print(" false -the first",n,"character are not same")

