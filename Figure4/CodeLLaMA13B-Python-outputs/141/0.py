def file_name_check(file_name):
    
    # Your code here
    if len(re.findall(r"\d", file_name)) > 3:
        return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 0:
        return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) > 1:
        return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == False:
            return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == True:
            return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == True:
            if file_name[-1] == ".":
                return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == True:
            if file_name[-1] != ".":
                return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == True:
            if file_name[-1] != ".":
                if file_name[-4:] != ".txt":
                    return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 1:
        if file_name[0].isalpha() == True:
            if file_name[-1] != ".":
                if file_name[-4:] != ".txt":
                    if file_name[-4:] != ".exe":
                        return "No"
    if len(re.findall(r"[a-zA-Z]", file_name)) == 