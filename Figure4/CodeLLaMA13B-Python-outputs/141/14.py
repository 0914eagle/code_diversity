def file_name_check(file_name):
    
    # your code here
    if len(re.findall(r'\d', file_name)) <= 3:
        if len(re.findall(r'\.', file_name)) == 1:
            if len(re.findall(r'[a-zA-Z]', file_name[:file_name.index('.')])) > 0:
                if file_name[file_name.index('.')+1:] in ['txt', 'exe', 'dll']:
                    return 'Yes'
    return 'No'


if __name__ == '__main__':
    print("Example:")
    print(file_name_check("example.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("example.1txt") == "No"
    assert file_name_check("example.") == "No"
    assert file_name_check("example") == "No"
    assert file_name_check(".txt") == "No"
    assert file_name_check("") == "No"
    assert file_name_check("123.456") == "No"
    assert file_name_check("123.dll") == "No"
    assert file_name_check("abc.123") == "No"
    assert file_name_check("abc.d") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"
    assert file_name_check("abc.123abc") == "No"