color_list1=input("enter color for color_list1(seperated by space):").split()
color_list2=input("enter color for color_list(seperated by space):").split()
colors_not_in_list2=[]
for color in color_list1:
    if color not in color_list2:
        colors_not_in_list2.append(color)
print("color from color_list1 not contained in color_list2:",colors_not_in_list2)    

