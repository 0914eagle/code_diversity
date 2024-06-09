
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    strongest_extension = None
    strongest_strength = -float('inf')
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension
        elif strength == strongest_strength:
            if extension < strongest_extension:
                strongest_extension = extension
    return f"{class_name}.{strongest_extension}"

