def fix_spaces(text):
    
    return re.sub(r'\s+', lambda x: '-' if len(x.group(0)) > 2 else '_', text)

