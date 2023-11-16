square_area=lambda side:side **2
rectangle_area=lambda length,width: length * width
triangle_area=lambda base,height: 0.5 * base * height
side_length=float(input("enter the side length of the square:"))
rectangle_length=float(input("enter the length of the rectangle:"))
rectangle_width=float(input("enter the width of the rectangle:"))
triangle_base=float(input("enter the base length of the triangle:"))
triangle_height=float(input("enter the height of the triangle:"))
print("Area of the square:",square_area(side_length))
print("Area of the reactangle:",rectangle_area(rectangle_length,rectangle_width))
print("Area of the traingle:",triangle_area(triangle_base,triangle_height))
