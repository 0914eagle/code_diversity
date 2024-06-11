def fix_spaces(text):
    
    if not text:
        return text
    text = text.replace(" ", "_")
    text = text.replace("__", "-")
    text = text.replace("--", "-")
    if text[0] == "_":
        text = text[1:]
    return text


