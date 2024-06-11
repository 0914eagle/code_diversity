def file_name_check(file_name):
    
    # Your code here
    if file_name.count('.') != 1:
        return 'No'
    else:
        file_name_split = file_name.split('.')
        if len(file_name_split[0]) == 0:
            return 'No'
        elif file_name_split[0][0].isalpha() == False:
            return 'No'
        elif file_name_split[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        elif file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
            return 'No'
        else:
            return 'Yes'

# print(file_name_check("example.txt")) # => 'Yes'
# print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
# print(file_name_check("1")) # => 'No' (the name should contain at least one letter)
# print(file_name_check("1.1")) # => 'No' (the name should contain only one dot)
# print(file_name_check("1.ttt")) # => 'No' (the substring after the dot should be one of these: ['txt', 'exe', 'dll'])
# print(file_name_check("file.name.doc")) # => 'No' (the name should contain only one dot)
# print(file_name_check("file.name.123.doc")) # => 'No' (the name should not contain more than three digits)
# print(file_name_check("file.name.1234.doc")) # => 'No' (the name should not contain more than three digits)
# print(file_name_check("file.name.12345.doc")) # => 'No' (the name should not contain more than three digits)
# print(file