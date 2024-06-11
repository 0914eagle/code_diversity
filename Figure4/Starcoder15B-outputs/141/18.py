def file_name_check(file_name):
    
    # Your code here
    if file_name.count(".") != 1:
        return "No"
    if file_name.count(".") > 3:
        return "No"
    if file_name.startswith("a-z") or file_name.startswith("A-Z"):
        return "No"
    if file_name.endswith("txt") or file_name.endswith("exe") or file_name.endswith("dll"):
        return "Yes"
    else:
        return "No"

# print(file_name_check("example.txt"))
# print(file_name_check("1example.dll"))
# print(file_name_check("example.txt.txt"))
# print(file_name_check("example.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("example.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt.txt"))
# print(file_name_check("