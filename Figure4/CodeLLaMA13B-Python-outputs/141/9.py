def file_name_check(file_name):
    
    # your code here
    if file_name.count(".") == 1:
        if file_name.count("0") <= 3 and file_name.count("1") <= 3 and file_name.count("2") <= 3 and file_name.count("3") <= 3 and file_name.count("4") <= 3 and file_name.count("5") <= 3 and file_name.count("6") <= 3 and file_name.count("7") <= 3 and file_name.count("8") <= 3 and file_name.count("9") <= 3:
            if file_name[0].isalpha():
                if file_name[-4:] == ".txt" or file_name[-4:] == ".exe" or file_name[-4:] == ".dll":
                    return "Yes"
                else:
                    return "No"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.123.dll"))
print(file_name_check("example.123"))
print(file_name_check("example.txt.dll"))
print(file_name_check("example.dll.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
print(file_name_check("example.txt"))
