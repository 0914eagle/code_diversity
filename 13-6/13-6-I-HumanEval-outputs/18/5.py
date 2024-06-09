
def file_name_check(file_name: str) -> str:
    
    if len(file_name) > 3 and file_name.count('.') != 1:
        return 'No'
    
    dot_index = file_name.index('.')
    before_dot = file_name[:dot_index]
    after_dot = file_name[dot_index+1:]
    
    if not before_dot.isalpha() or not after_dot in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

