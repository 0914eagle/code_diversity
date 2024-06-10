
import re

def has_valid_format(file_name: str) -> bool:
    return re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[txt|exe|dll]$', file_name) is not None

def has_valid_digits(file_name: str) -> bool:
    return sum(1 for char in file_name if char.isdigit()) <= 3

def file_name_check(file_name: str) -> str:
    if '.' not in file_name:
        return 'No'
    
    file_parts = file_name.split('.')
    if len(file_parts) != 2:
        return 'No'
    
    if not has_valid_digits(file_parts[0]):
        return 'No'
    
    if not has_valid_format(file_name):
        return 'No'
    
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(file_name_check(file_name))
