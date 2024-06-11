def file_name_check(file_name):
    
    # your code here
    # return 'Yes' if the the file's name is valid, and returns 'No' otherwise.
    if file_name.count(".") == 1:
        if file_name.count(".") == 1 and file_name[0].isalpha():
            if file_name.count(".") == 1 and file_name[-3:].isdigit():
                if file_name.count(".") == 1 and file_name[-3:].isdigit():
                    if file_name[-3:] == "txt" or file_name[-3:] == "exe" or file_name[-3:] == "dll":
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
print(file_name_check("example.txts"))
print(file_name_check("example.txt."))
print(file_name_check("example."))
print(file_name_check("example"))
print(file_name_check("e.tx"))
print(file_name_check("e.txt"))
print(file_name_check("e.txtt"))
print(file_name_check("e.dll"))
print(file_name_check("e.dlll"))
print(file_name_check("e.dlls"))
print(file_name_check("e.dll."))
print(file_name_check("e.dlls"))
print(file_name_check("e.exe"))
print(file_name_check("e.exee"))
print(file_name_check("e.exe."))
print(file_name_check("e.exee"))
print(file_name_check("e.exe."))
print(file_name_check("e.exee"))
print(file_name_check("e.exee"))
print(file_name_check("e.exee"))
