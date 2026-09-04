def check_right_angled_triangle(side1, side2, side3):
    if side1*side1 + side2*side2 == side3*side3:
        print("Triangle is Right-angled")
    elif side1*side1 + side3*side3 == side2*side2:
        print("Triangle is Right-angled")
    elif side2*side2 + side3*side3 == side1*side1:
        print("Triangle is Right-angled")
    else:
        print("Triangle is Not Right-angled")


side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

check_right_angled_triangle(side1, side2, side3)