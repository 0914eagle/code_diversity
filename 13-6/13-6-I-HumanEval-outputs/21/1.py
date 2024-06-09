
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Find the strongest extension by calculating the strength of each extension
    # and returning the extension with the highest strength
    strongest_extension = None
    strongest_strength = -float('inf')
    for extension in extensions:
        strength = _calculate_strength(extension)
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    # Return the strongest extension in the format ClassName.StrongestExtensionName
    return f"{class_name}.{strongest_extension}"

def _calculate_strength(extension: str) -> float:
    
    cap = sum(1 for c in extension if c.isupper())
    sm = sum(1 for c in extension if c.islower())
    return cap - sm


