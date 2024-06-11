def fix_spaces(text):
    
    if not text:
        return text
    text = text.replace(" ", "_")
    text = re.sub(r"\s+", "-", text)
    return text


