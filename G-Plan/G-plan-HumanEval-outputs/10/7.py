
import re

def has_valid_extension(file_name):
    return file_name.split('.')[-1] in ['txt', 'exe', 'dll']

def file_name_check(file_name):
    if not re.match(r'^[a-zA-Z][^0-9]*\.[0-9]{0,3}[a-zA-Z]+$', file_name):
        return 'No'
    if not has_valid_extension(file_name):
        return 'No'
    return 'Yes'

if __name__ == "__main__":
    file_name = input().strip()
    print(file_name_check(file_name))
