def file_name_check(file_name):
    
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('.') > 3:
        return 'No'
    if file_name.count('.') == 1:
        if file_name.split('.')[0] == '':
            return 'No'
        if file_name.split('.')[0][0] not in string.ascii_letters:
            return 'No'
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return 'No'
    return 'Yes'

# print(file_name_check("example.txt"))
# print(file_name_check("1example.dll"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.14.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.txt"))
# print(file_name_check("1.2.3.4.5.6.7.8.9.10.11.12.13.14.15