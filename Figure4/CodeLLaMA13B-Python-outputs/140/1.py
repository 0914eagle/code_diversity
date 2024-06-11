def fix_spaces(text):
    
    if text == "":
        return ""
    if text[0] == " ":
        text = "_" + text[1:]
    if text[-1] == " ":
        text = text[:-1] + "_"
    if "  " in text:
        text = text.replace("  ", "-")
    if "__" in text:
        text = text.replace("__", "_")
    return text


