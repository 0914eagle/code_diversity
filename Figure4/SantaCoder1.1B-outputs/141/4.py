def file_name_check(file_name):
    
    if len(file_name) > 3:
        return "No"
    if file_name.count(".") != 1:
        return "No"
    if file_name[0] not in "abc