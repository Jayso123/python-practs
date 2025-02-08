def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

print(f"Area: {area(length, width)}")
print(f"Perimeter: {perimeter(length, width)}")
