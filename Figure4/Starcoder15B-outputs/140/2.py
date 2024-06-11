def fix_spaces(text):
    
    return re.sub(r' +', '-', re.sub(r' ', '_', text))


