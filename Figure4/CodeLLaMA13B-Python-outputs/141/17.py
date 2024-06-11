def file_name_check(file_name):
    
    # Your code here
    # return 'Yes' if the file name is valid, and return 'No' otherwise
    if file_name.count(".") == 1:
        if file_name.count(".") == 1:
            if file_name.startswith("."):
                return "No"
            else:
                if file_name.endswith(".") or file_name.endswith(".."):
                    return "No"
                else:
                    if file_name.endswith(".txt") or file_name.endswith(".exe") or file_name.endswith(".dll"):
                        if file_name.count("0") <= 3 and file_name.count("1") <= 3 and file_name.count("2") <= 3 and file_name.count("3") <= 3 and file_name.count("4") <= 3 and file_name.count("5") <= 3 and file_name.count("6") <= 3 and file_name.count("7") <= 3 and file_name.count("8") <= 3 and file_name.count("9") <= 3:
                            if file_name[0].isalpha():
                                return "Yes"
                            else:
                                return "No"
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
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.txt"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.txt"))
print(file_name_check("example.exe"))
print(file_name_check("example.dll"))
print(file_name_check("example.txt"))
print(file_name_check("example.exe"))
print(file_name_check("example.