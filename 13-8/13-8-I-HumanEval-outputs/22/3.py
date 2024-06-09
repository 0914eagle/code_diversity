
def file_name_check(file_name: str) -> str:
    
    # Check if the file name contains more than three digits
    if file_name.count('0', '9') > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is not empty and starts with a letter
    if not file_name.split('.')[0].strip() or not file_name.split('.')[0].strip().isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

