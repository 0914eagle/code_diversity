def file_name_check(file_name):
    
    # Your code here
    # check if there are more than 3 digits
    if len([i for i in file_name if i.isdigit()]) > 3:
        return 'No'
    # check if there is only one dot
    if file_name.count('.') != 1:
        return 'No'
    # check if the substring before the dot is not empty and starts with a letter from the latin alphapet
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    # check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

# print(file_name_check("example.txt")) # => 'Yes'
# print(file_name_check("1example.dll")) # => 'No' (the name should start with a latin alphapet letter)

