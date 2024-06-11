def fix_spaces(text):
    
    return re.sub(r' +', '-', text.replace(' ', '_'))

