
def file_name_check(file_name: str) -> str:
    

    # Split the file name into the substring before and after the dot
    substring_before_dot, substring_after_dot = file_name.split('.')

    # Check if the file name contains more than three digits
    if substring_before_dot.isdigit() and len(substring_before_dot) > 3:
        return 'No'

    # Check if the file name contains exactly one dot
    if substring_before_dot.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is empty
    if not substring_before_dot:
        return 'No'

    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not substring_before_dot[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if substring_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    # If all conditions are met, return 'Yes'
    return 'Yes'

