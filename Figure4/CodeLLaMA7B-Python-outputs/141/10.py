def file_name_check(file_name):
    
    # Your code here
    if file_name.count('.') > 1:
        return 'No'
    if file_name.count('.') == 0:
        return 'No'
    if file_name.count('.') == 1:
        if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
            return 'No'
        if file_name[0].isalpha() == False:
            return 'No'
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return 'No'
    return 'Yes'

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.exe.exe")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll.exe")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll.dll.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.dll.dll.dll.dll")) # => 'No'