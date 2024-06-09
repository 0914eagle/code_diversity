
from typing import Optional

def string_to_md5(text: str) -> Optional[str]:
    
    import hashlib
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

