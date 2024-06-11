def file_name_check(file_name):
    
    if len(file_name) > 3:
        return "No"
    if file_name.count(".") != 1:
        return "No"
    if not file_name.startswith("."):
        return "No"
    if file_name.endswith(".exe") or file_name.endswith(".dll"):
        return "Yes"
    return "No"


