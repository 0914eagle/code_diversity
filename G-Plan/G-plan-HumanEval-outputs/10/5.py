
import re

def check_digits(file_name):
    return sum(1 for char in file_name if char.isdigit())

def check_file_extension(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    return file_name.split('.')[-1] in valid_extensions

def file_name_check(file_name):
    if check_digits(file_name) > 3:
        return 'No'
    
    if file_name.count('.') != 1:
        return 'No'
    
    file_parts = file_name.split('.')
    if not file_parts[0] or not file_parts[0][0].isalpha():
        return 'No'
    
    if not check_file_extension(file_name):
        return 'No'
    
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(file_name_check(file_name))
