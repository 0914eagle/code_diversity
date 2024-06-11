def file_name_check(file_name):
    
    # Your code here
    if len(file_name) > 10:
        return "No"
    if file_name.count(".") != 1:
        return "No"
    if file_name[0].isalpha() == False:
        return "No"
    if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
        return "No"
    if len(file_name.split(".")[0]) == 0:
        return "No"
    if len(file_name.split(".")[0]) > 3:
        return "No"
    if file_name.count(".") > 1:
        return "No"
    if file_name.count(".") == 1:
        if file_name.split(".")[0].isdigit() == True:
            return "No"
        if file_name.split(".")[1].isdigit() == True:
            return "No"
    return "Yes"

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.dll"))
print(file_name