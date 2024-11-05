area_square=lambda side:side*side
area_rectangle=lambda length,width:length*width
area_triangle=lambda base,height:0.5 *base*height
side=float(input("enter the side of the square:"))
print("area of square:",area_square(side))
length=float(input("enter the length of rectangle:"))
width=float(input("enter the width of the rectangle:"))
print("area of rectangle:",area_rectangle(length,width))
base=float(input("enter the base of triangle:"))
height=float(input("enter the height of triangle:"))
print("area of triangle:",area_triangle(base,height))

