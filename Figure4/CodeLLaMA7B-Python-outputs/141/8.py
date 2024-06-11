def file_name_check(file_name):
    
    # Your code here
    if file_name.count(".") > 1:
        return "No"
    elif file_name.count(".") == 1:
        if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
            return "No"
        elif file_name[0].isalpha() == False:
            return "No"
        elif file_name[-3:] != "txt" and file_name[-3:] != "exe" and file_name[-3:] != "dll":
            return "No"
        else:
            return "Yes"
    else:
        return "No"

print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
print(file_name_check("example.exe")) # => 'Yes'
print(file_name_check("example.exe.exe")) # => 'No' (there should not be more than one dot in the file's name)
print(file_name_check("example.dll.exe")) # => 'No' (the substring after the dot should be one of these: ['txt', 'exe', 'dll'])
print(file_name_check("example.dll.exe.exe")) # => 'No' (there should not be more than one dot in the file's name)
print(file_name_check("example.exe.dll.exe")) # => 'No' (the substring after the dot should be one of these: ['txt', 'exe', 'dll'])
print(file_name_check("example.exe.dll.exe.exe")) # => 'No' (there should not be more than one dot