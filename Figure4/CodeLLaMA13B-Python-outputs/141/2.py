def file_name_check(file_name):
    
    # your code here
    if len(file_name) == 0:
        return "No"
    if file_name.count(".") != 1:
        return "No"
    if file_name[0].isalpha() == False:
        return "No"
    if file_name[-4:] != ".txt" and file_name[-4:] != ".exe" and file_name[-4:] != ".dll":
        return "No"
    if file_name.count("0") > 3 or file_name.count("1") > 3 or file_name.count("2") > 3 or file_name.count("3") > 3 or file_name.count("4") > 3 or file_name.count("5") > 3 or file_name.count("6") > 3 or file_name.count("7") > 3 or file_name.count("8") > 3 or file_name.count("9") > 3:
        return "No"
    return "Yes"

print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))