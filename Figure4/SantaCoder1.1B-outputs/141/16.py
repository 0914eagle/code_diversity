def file_name_check(file_name):
    
    if len(file_name) > 3:
        return "No"
    if file_name[0] != '.':
        return "No"
    if file_name[1] != '.':
        return "No"
    if file_name[2] != '.':
        return "No"
    if file_name[3] not in ['txt', 'exe', 'dll']:
        return "No"
    if file_name[4] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        return "No"
    return "Yes"

