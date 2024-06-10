
import re

def check_digits(file_name):
    return sum(1 for char in file_name if char.isdigit())

def check_file_extension(file_name):
    extensions = ['txt', 'exe', 'dll']
    return file_name.split('.')[-1] in extensions

def check_file_name(file_name):
    if file_name.count('.') != 1:
        return 'No'
    
    before_dot, after_dot = file_name.split('.')
    
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    if check_digits(before_dot) > 3:
        return 'No'
    
    if not check_file_extension(file_name):
        return 'No'
    
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(check_file_name(file_name))
