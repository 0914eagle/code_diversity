def file_name_check(file_name):
    
    if file_name.count(".") > 1:
        return "No"
    elif file_name.count(".") == 0:
        return "No"
    elif file_name.count(".") == 1:
        if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
            return "No"
        elif file_name[0].isalpha() == False:
            return "No"
        elif file_name.split(".")[1] not in ["txt", "exe", "dll"]:
            return "No"
        else:
            return "Yes"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.txt.exe"))
print(file_name_check("example.txt.exe.dll"))
print(file_name_check("example.exe.dll.txt"))
print(file_name_check("example.exe.dll.exe"))
print(file_name_check("example.exe.exe.exe"))
print(file_name_check("example.exe.dll.exe.txt"))
print(file_name_check("example.exe.exe.dll.exe.txt"))
print(file_name_check("example.exe.dll.exe.exe.txt"))
print(file_name_check("example.exe.exe.dll.exe.exe.txt"))
print(file_name_check("example.exe.exe.dll.exe.exe