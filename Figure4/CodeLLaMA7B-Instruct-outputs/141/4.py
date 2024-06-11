

def file_name_check(file_name):
    

    # Check if the file name contains more than three digits
    if file_name.isdigit() and len(file_name) > 3:
        return 'No'

    # Check if the file name contains a dot
    if '.' not in file_name:
        return 'No'

    # Check if the substring before the dot is empty or not
    if file_name.split('.')[0] == '':
        return 'No'

    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not file_name.split('.')[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


