#!/usr/bin/env python3
def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
result = pow(2, 2)
print(result)  