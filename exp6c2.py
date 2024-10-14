l1=list(map(int,input("enter the first list of integers(space_seperated):").split()))
l2=list(map(int,input("enter the  second  list of integers(space_seperated):").split()))
if len(l1)==len(l2):
    print("the two lists are of the same length")
else:
    print("the two lists are not same length")
if sum(l1)==sum(l2):
    print("the two lists sum is same value")
else:
    print("the two lists sum is not same value")
common_value=set(l1).intersection (set(l2))
if common_value:
    print("common values between the list",common_value)
else:
    print("no common values between the list")  
