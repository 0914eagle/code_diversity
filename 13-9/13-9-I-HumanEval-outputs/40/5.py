
from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    
    import hashlib
    if text == '':
        return None
    md5 = hashlib.md5(text.encode())
    return md5.hexdigest()

