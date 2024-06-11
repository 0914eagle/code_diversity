

def file_name_check(file_name):
    
    # Check if the file name has more than three digits
    if len(file_name) - file_name.count('0') - file_name.count('1') - file_name.count('2') - file_name.count('3') - file_name.count('4') - file_name.count('5') - file_name.count('6') - file_name.count('7') - file_name.count('8') - file_name.count('9') > 3:
        return 'No'

    # Check if the file name contains more than one dot
    if file_name.count('.') != 1:
        return 'No'

    # Check if the substring before the dot is empty or not
    if file_name.split('.')[0] == '':
        return 'No'

    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not file_name.split('.')[0][0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of the allowed extensions
    if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'


