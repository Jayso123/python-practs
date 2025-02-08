def convert_base(number, from_base, to_base):
    decimal = int(number, from_base)
    if to_base == 10:
        return decimal
    else:
        result = ""
        while decimal > 0:
            result = str(decimal % to_base) + result
            decimal = decimal // to_base
        return result if result else "0"

number = input("Enter the number: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the target base: "))
print(f"Converted number: {convert_base(number, from_base, to_base)}")
