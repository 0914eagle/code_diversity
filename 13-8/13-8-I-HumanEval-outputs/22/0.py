
def file_name_check(file_name: str) -> str:
    
    # check if the file name contains more than three digits
    if file_name.count("0", "9") > 3:
        return "No"
    
    # check if the file name contains exactly one dot
    if file_name.count(".") != 1:
        return "No"
    
    # check if the substring before the dot is not empty and starts with a letter from the latin alphabet
    substring_before_dot = file_name.split(".")[0]
    if len(substring_before_dot) == 0 or not substring_before_dot[0].isalpha():
        return "No"
    
    # check if the substring after the dot is one of the allowed extensions
    substring_after_dot = file_name.split(".")[1]
    if substring_after_dot not in ["txt", "exe", "dll"]:
        return "No"
    
    return "Yes"

