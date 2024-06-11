def file_name_check(file_name):
    
    # Your code here
    # Check if there are more than 3 digits
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    # Check if there is a dot
    if '.' not in file_name:
        return 'No'
    # Check if the substring before the dot is empty
    if file_name.split('.')[0] == '':
        return 'No'
    # Check if the substring before the dot starts with a latin alphapet
    if not file_name.split('.')[0][0].isalpha():
        return 'No'
    # Check if the substring after the dot is one of the three options
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'


print(file_name_check("example.txt"))
print(file_name_check("1example.dll"))
