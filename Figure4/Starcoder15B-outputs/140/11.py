def fix_spaces(text):
    
    text = text.replace(" ", "_")
    text = re.sub(r"_{2,}", "-", text)
    return text

