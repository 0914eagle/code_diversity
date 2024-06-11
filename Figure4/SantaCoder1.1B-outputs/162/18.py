def string_to_md5(text):
    
    if text:
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    else:
        return None


