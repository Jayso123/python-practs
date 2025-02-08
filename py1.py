def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp = float(input("Enter temperature: "))
unit = input("Is the temperature in Fahrenheit (F) or Celsius (C)? ").upper()

if unit == "F":
    print(f"{temp} Fahrenheit is equal to {fahrenheit_to_celsius(temp):.2f} Celsius.")
elif unit == "C":
    print(f"{temp} Celsius is equal to {celsius_to_fahrenheit(temp):.2f} Fahrenheit.")
else:
    print("Invalid unit.")
