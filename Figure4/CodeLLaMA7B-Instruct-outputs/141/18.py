

def file_name_check(file_name):
    
    # Check if the file name contains more than three digits
    if len(file_name.split('.')) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if len(file_name.split('.')) != 2:
        return 'No'

    # Check if the substring before the dot is not empty and starts with a letter
    if file_name.split('.')[0] == '' or not file_name.split('.')[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


