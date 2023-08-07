#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Test the function
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)

