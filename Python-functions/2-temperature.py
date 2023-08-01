#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
result = convert_to_celsius (100)
print(result)

result = convert_to_celsius (-40)
print(result)

result = convert_to_celsius (-459.67)
print(result)

result = convert_to_celsius (32)
print(result)