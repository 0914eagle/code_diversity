
import re

def has_valid_extension(file_name):
    return file_name.split('.')[-1] in ['txt', 'exe', 'dll']

def file_name_check(file_name):
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'
    
    if not has_valid_extension(file_name):
        return 'No'
    
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(file_name_check(file_name))
