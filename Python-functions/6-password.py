#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if ' ' in password:
        return False
    return True
result = validate_password("Password123")
print(result) 

result = validate_password("abc123")
print(result)  

result = validate_password("Password 123")
print(result) 

result = validate_password("password123")
print(result)