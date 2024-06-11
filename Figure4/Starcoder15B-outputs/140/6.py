def fix_spaces(text):
    
    return re.sub(r' {2,}', '-', re.sub(r' ', '_', text))

