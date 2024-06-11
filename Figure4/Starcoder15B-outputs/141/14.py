def file_name_check(file_name):
    
    # Your code here
    # check if there are more than 3 digits
    if len(re.findall(r'\d{4,}', file_name)) > 0:
        return 'No'
    # check if there is exactly one dot
    if len(re.findall(r'\.', file_name)) != 1:
        return 'No'
    # check if the substring before the dot is empty
    if len(re.findall(r'^[a-zA-Z]+\.', file_name)) == 0:
        return 'No'
    # check if the substring after the dot is one of the given options
    if len(re.findall(r'\.(txt|exe|dll)$', file_name)) == 0:
        return 'No'
    return 'Yes'

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("1example.d")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dlll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dlllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dllllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dlllllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dllllllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dlllllllll")) # => 'No' (the name should end with one of the given options)
print(file_name_check("1example.dllllllllll")) # => 'No' (