def fix_spaces(text):
    
    if len(text) <= 2:
        return text
    else:
        return text.replace(" ", "_").replace("  ", "-")

