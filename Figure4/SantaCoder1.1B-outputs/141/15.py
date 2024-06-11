def file_name_check(file_name):
    
    if len(file_name) > 3:
        return "No"
    if file_name.find(".") == -1:
        return "No"
    if file_name[0] != "." or file_name[-1] != ".":
        return "No"
    if file_name[0].isalpha() == False or file_name[-1].isalpha() == False:
        return "No"
    if file_name[0] not in string.ascii_letters or file_name[-1] not in string.ascii_letters:
        return "No"
    if file_name[0] == file_name[-1] and file_name[0] not in string.ascii_letters:
        return "No"
    if file_name[0] == file_name[-1] and file_name[0] in string.ascii_letters:
        return "No"
    if file_name[0] == file_name[-1] and file_name[0] in string.ascii_letters:
        return "No"
    return "Yes"

