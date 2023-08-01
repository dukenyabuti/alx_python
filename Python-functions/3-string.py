#!/usr/bin/env python3
def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
result = reverse_string("Hello")
print(result)  

result = reverse_string(" ")
print(result)  

result = reverse_string("madam")
print(result)  

result = reverse_string("Hello, World!")
print(result)  