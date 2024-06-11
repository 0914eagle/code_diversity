def file_name_check(file_name):
    
    # your code here
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif file_name[0].isalpha() == False:
        return 'No'
    elif file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    else:
        return 'Yes'


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.1txt") == "No"
    assert file_name_check("example.") == "No"
    assert file_name_check("example.1") == "No"
    assert file_name_check("example..txt") == "No"
    assert file_name_check(".example.txt") == "No"
    assert file_name_check("example.1.txt") == "No"
    assert file_name_check("example.txt1") == "No"
    assert file_name_check("example.exe") == "Yes"
    assert file_name_check("example.dll") == "Yes"
    assert file_name_check("example.txtexe") == "No"
    assert file_name_check("example.") == "No"
    assert file_name_check("example") == "No"
    assert file_name_check(".example") == "No"
    assert file_name_check("example.exe.txt") == "No"
    print("Coding complete? Click 'Check' to earn cool rewards!")
