def string_to_md5(text):
    
    if text == '':
        return None
    import hashlib
    return hashlib.md5(text.encode('utf-8')).hexdigest()


