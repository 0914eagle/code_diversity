def file_name_check(file_name):
    
    # Your code here
    import re
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    elif len(re.findall(r'\.', file_name)) != 1:
        return 'No'
    elif len(re.findall(r'[a-zA-Z]', file_name[0])) == 0:
        return 'No'
    elif file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.txt.dll"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.dll.dll"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.dll.txt"))
print(file_name_check("example.txt.txt"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.txt.exe"))
print(file_name_check("example.txt.txt"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.txt.exe"))
print(file_name_check("example.dll.txt"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.dll.dll"))
print(file_name_check("example.txt.dll"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.dll.dll"))
print(file_name_check("example.txt.txt"))
print(file_name_check("example.exe.txt"))
