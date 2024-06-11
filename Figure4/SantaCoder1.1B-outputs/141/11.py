def file_name_check(file_name):
    
    # Your code here
    if len(file_name) > 3:
        return "No"
    elif file_name.count(".") != 1:
        return "No"
    elif file_name[0] not in "abc