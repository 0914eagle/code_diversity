def file_name_check(file_name):
    
    # Your code here
    import re
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif re.findall(r'\.', file_name)[0] == '.':
        return 'No'
    elif re.findall(r'\.', file_name)[0] != '.':
        if file_name[0].isalpha() == False:
            return 'No'
        elif file_name[0].isalpha() == True:
            if file_name[file_name.find('.') - 1].isalpha() == False:
                return 'No'
            elif file_name[file_name.find('.') - 1].isalpha() == True:
                if file_name[file_name.find('.') + 1:] in ['txt', 'exe', 'dll']:
                    return 'Yes'
                else:
                    return 'No'


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.exe.exe"))
print(file_name_check("example.dll.dll"))
print(file_name_check("example.txt.txt"))
print(file_name_check("example.txt.exe"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.dll.txt"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.exe.dll.exe"))
print(file_name_check("example.dll.dll.exe"))
print(file_name_check("example.dll.dll.exe.exe"))
print(file_name_check("example.dll.dll.exe.exe.exe"))
print(file_name_