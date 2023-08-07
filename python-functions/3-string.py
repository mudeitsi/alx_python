#!/usr/bin/python3
def reverse_string(string):
    reversed_str = string[::-1]
    return reversed_str

# Test the function
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

