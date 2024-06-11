def file_name_check(file_name):
    
    # Your code here
    if len(file_name) == 0:
        return 'No'
    else:
        if file_name.count('.') == 1:
            if file_name.count('0') <= 3 and file_name.count('1') <= 3 and file_name.count('2') <= 3 and file_name.count('3') <= 3 and file_name.count('4') <= 3 and file_name.count('5') <= 3 and file_name.count('6') <= 3 and file_name.count('7') <= 3 and file_name.count('8') <= 3 and file_name.count('9') <= 3:
                if file_name[0].isalpha():
                    if file_name.split('.')[1] in ['txt', 'exe', 'dll']:
                        return 'Yes'
                    else:
                        return 'No'
                else:
                    return 'No'
            else:
                return 'No'
        else:
            return 'No'


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.1txt") == "No"
    assert file_name_check("example.") == "No"
    assert file_name_check("example.123") == "No"
    assert file_name_check("example.dll.exe") == "No"
    assert file_name_check("example.dll.123") == "No"
    assert file_name_check("example.exe.") == "No"
    assert file_name_check("example.exe.123") == "No"
    assert file_name_check("example.123.dll") == "No"
    assert file_name_check("example.123.exe")