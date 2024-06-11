def string_to_md5(text):
    
    import hashlib
    if text:
        return hashlib.md5(text.encode()).hexdigest()
    else:
        return None


