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
        elif file_name_split[0].count('0') + file_name_split[0].count('1') + file_name_split[0].count('2') + file_name_split[0].count('3') + file_name_split[0].count('4') + file_name_split[0].count('5') + file_name_split[0].count('6') + file_name_split[0].count('7') + file_name_split[0].count('8') + file_name_split[0].count('9') > 3:
            return 'No'
        else:
            return 'Yes'

# print(file_name_check("example.txt")) # => 'Yes'
# print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)
# print(file_name_check("1")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2.3")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2.3.4")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2.3.4.5")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2.3.4.5.6")) # => 'No' (the name should contain a dot)
# print(file_name_check("1.2.3.4.5.6.