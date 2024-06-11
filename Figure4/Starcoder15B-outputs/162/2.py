def string_to_md5(text):
    
    if not text:
        return None
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


