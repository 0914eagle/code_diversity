
import re

def has_valid_number_of_digits(file_name):
    return sum(1 for char in file_name if char.isdigit()) <= 3

def has_valid_dot_count(file_name):
    return file_name.count('.') == 1

def has_valid_prefix(file_name):
    return re.match(r'^[a-zA-Z].*', file_name.split('.')[0]) is not None

def has_valid_extension(file_name):
    return file_name.split('.')[-1] in ['txt', 'exe', 'dll']

def file_name_check(file_name):
    if not has_valid_number_of_digits(file_name):
        return 'No'
    if not has_valid_dot_count(file_name):
        return 'No'
    if not has_valid_prefix(file_name):
        return 'No'
    if not has_valid_extension(file_name):
        return 'No'
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(file_name_check(file_name))
