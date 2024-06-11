def file_name_check(file_name):
    
    # your code here
    # return 'Yes' if the the file's name is valid, and returns 'No' otherwise.
    if file_name.count(".") == 1:
        if file_name.count(".") == 1 and file_name[0].isalpha() and file_name[-4:] in [".txt", ".exe", ".dll"]:
            if file_name.count("0") <= 3 and file_name.count("1") <= 3 and file_name.count("2") <= 3 and file_name.count("3") <= 3 and file_name.count("4") <= 3 and file_name.count("5") <= 3 and file_name.count("6") <= 3 and file_name.count("7") <= 3 and file_name.count("8") <= 3 and file_name.count("9") <= 3:
                return "Yes"
            else:
                return "No"
        else:
            return "No"
    else:
        return "No"


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
print(file_name_check("example.exe"))
print(file_name_check("example.txts"))
print(file_name_check("example"))
print(file_name_check("e.tx"))
print(file_name_check("exampl.txt"))
print(file_name_check("e45.txt"))
print(file_name_check("e4.tx5t"))
print(file_name_check("e.e"))
print(file_name_check("e.ex"))
print(file_name_check("e.t"))
print(file_name_check("e.tx5"))
print(file_name_check("e.txe"))
print(file_name_check("e.t5"))
print(file_name_check("e.t5"))
print(file_name_check("e.t5"))
print(file_name_check("e.t5"))
print(file_name_check("e.t5"))
print(file