def file_name_check(file_name):
    
    # Your code here
    import re
    if re.search(r'[0-9]', file_name):
        return 'No'
    elif file_name.count('.') > 1:
        return 'No'
    elif file_name.count('.') < 1:
        return 'No'
    elif file_name.count('.') == 1:
        if re.search(r'[a-zA-Z]', file_name[:file_name.find('.')]) == None:
            return 'No'
        elif file_name[file_name.find('.') + 1:] not in ['txt', 'exe', 'dll']:
            return 'No'
    return 'Yes'


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.exe.dll.txt"))
print(file_name_check("example.exe.dll.exe"))
print(file_name_check("example.exe.dll.exe.txt"))
print(file_name_check("example.exe.dll.exe.dll"))
print(file_name_check("example.exe.dll.exe.dll.txt"))
print(file_name_check("example.exe.dll.exe.dll.exe"))
print(file_name_check("example.exe.dll.exe.dll.exe.txt"))
print(file_name_check("example.exe.dll.exe.dll.exe.dll"))
print(file_name_check("example.exe.dll.exe.dll.exe.dll.txt"))
print(file_name_check("example.exe.dll.exe.dll.exe.dll.exe"))
print(file_name_check("example.exe.dll.exe.dll.exe.dll.exe.txt"))
print(file_name_check("example.exe.dll.exe.dll.exe.