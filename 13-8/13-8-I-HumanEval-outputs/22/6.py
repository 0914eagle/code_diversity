
def file_name_check(file_name: str) -> str:
    
    # Check if the file name contains more than three digits
    if len([char for char in file_name if char.isdigit()]) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is not empty and starts with a letter
    substring_before_dot = file_name.split('.')[0]
    if len(substring_before_dot) == 0 or not substring_before_dot[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    substring_after_dot = file_name.split('.')[1]
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

