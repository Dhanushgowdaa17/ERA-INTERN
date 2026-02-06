def calc_rectangle_area(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))  
area, perimeter = calc_rectangle_area(length, width)
print("Area:", area,
      "Perimeter:", perimeter)