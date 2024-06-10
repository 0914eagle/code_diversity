
import re

def check_digits(file_name):
    return sum(1 for char in file_name if char.isdigit())

def check_file_name(file_name):
    if check_digits(file_name) > 3:
        return 'No'
    
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'
    
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(check_file_name(file_name))
