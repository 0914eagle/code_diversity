def fix_spaces(text):
    
    if text == "":
        return ""
    if text[0] == " ":
        return "_" + fix_spaces(text[1:])
    if text[0] != " ":
        if text[1] == " ":
            if text[2] == " ":
                return text[0] + "-" + fix_spaces(text[2:])
            else:
                return text[0] + "_" + fix_spaces(text[1:])
        else:
            return text[0] + fix_spaces(text[1:])


if