def file_name_check(file_name):
    
    # your code here
    if len(re.findall(r"\d", file_name)) > 3:
        return "No"
    elif file_name.count(".") != 1:
        return "No"
    elif file_name.split(".")[0] == "":
        return "No"
    elif file_name.split(".")[1] not in ["txt", "exe", "dll"]:
        return "No"
    elif not file_name[0].isalpha():
        return "No"
    else:
        return "Yes"
