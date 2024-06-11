def file_name_check(file_name):
    
    # Your code here
    import re
    pattern = re.compile(r'[a-zA-Z]\w*\.\w{3}')
    if pattern.match(file_name):
        return 'Yes'
    else:
        return 'No'

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.txt1"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(file_name_check("example.txtt"))
print(