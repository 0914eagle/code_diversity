def file_name_check(file_name):
    
    # Your code here
    # 1. There should not be more than three digits ('0'-'9') in the file's name.
    # 2. The file's name contains exactly one dot '.'
    # 3. The substring before the dot should not be empty, and it starts with a letter from 
    # the latin alphapet ('a'-'z' and 'A'-'Z').
    # 4. The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    # 1.
    if file_name.count('0') > 3 or file_name.count('1') > 3 or file_name.count('2') > 3 or file_name.count('3') > 3 or file_name.count('4') > 3 or file_name.count('5') > 3 or file_name.count('6') > 3 or file_name.count('7') > 3 or file_name.count('8') > 3 or file_name.count('9') > 3:
        return 'No'
    # 2.
    if file_name.count('.') != 1:
        return 'No'
    # 3.
    if file_name.startswith('0') or file_name.startswith('1') or file_name.startswith('2') or file_name.startswith('3') or file_name.startswith('4') or file_name.startswith('5') or file_name.startswith('6') or file_name.startswith('7') or file_name.startswith('8') or file_name.startswith('9'):
        return 'No'
    # 4.
    if file_name.endswith('txt') or file_name.endswith('exe') or file_name.endswith('dll'):
        return 'Yes'
    else:
        return 'No'

#