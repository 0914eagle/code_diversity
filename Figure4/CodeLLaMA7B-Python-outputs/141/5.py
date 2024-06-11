def file_name_check(file_name):
    
    if file_name.count(".") > 1:
        return "No"
    elif file_name.count(".") == 1:
        if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
            return "No"
        elif file_name.count(".") == 1:
            if file_name.count(".") == 1:
                if file_name.split(".")[0].isalpha() == False:
                    return "No"
                elif file_name.split(".")[1] != "txt" and file_name.split(".")[1] != "exe" and file_name.split(".")[1] != "dll":
                    return "No"
                else:
                    return "Yes"
            else:
                return "No"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.exe.dll.exe"))
print(file_name_check("example.exe.dll.exe.exe"))
print(file_name_check("example.exe.dll.exe.exe.exe"))
print(file_name_check("example.exe.dll.exe.exe.exe.exe"))
print(file_name_check("example.exe.dll.exe.exe.exe.exe.exe"))
print(file_name_