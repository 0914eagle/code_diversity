def file_name_check(file_name):
    
    # Your code here
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 1:
        if file_name.count("0") > 2 or file_name.count("1") > 2 or file_name.count("2") > 2 or file_name.count("3") > 2 or file_name.count("4") > 2 or file_name.count("5") > 2 or file_name.count("6") > 2 or file_name.count("7") > 2 or file_name.count("8") > 2 or file_name.count("9") > 2:
            return "No"
        if file_name.count(".") == 1:
            if file_name[0].isalpha() == False:
                return "No"
            if file_name.split(".")[1] != "txt" and file_name.split(".")[1] != "exe" and file_name.split(".")[1] != "dll":
                return "No"
    return "Yes"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe.txt"))
print(file_name_check("example.exe.dll"))
print(file_name_check("example.exe.dll.txt"))
print(file_name_check("example.exe.dll.txt.exe"))
print(file_name_check("example.exe.dll.txt.exe.txt"))
