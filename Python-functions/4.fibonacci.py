#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_value = sequence[i-1] + sequence[i-2]
            sequence.append(next_value)
        return sequence
result = fibonacci_sequence(6)
print(result)  

result = fibonacci_sequence(1)
print(result)  

result = fibonacci_sequence(0)
print(result)  
    
result = fibonacci_sequence(20)
print(result)    