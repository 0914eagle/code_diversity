def file_name_check(file_name):
    
    # your code here
    if len(re.findall(r"\d", file_name)) > 3:
        return "No"
    if file_name.count(".") != 1:
        return "No"
    if file_name.split(".")[0] == "":
        return "No"
    if file_name.split(".")[1] not in ["txt", "exe", "dll"]:
        return "No"
    if not file_name[0].isalpha():
        return "No"
    return "Yes"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll"))
print(file_name_check("123example.exe"))
print(file_name_check("123example.txt"))
print(file_name_check("123example.dll