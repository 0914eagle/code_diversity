
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def calculate_strength(extension: str) -> float:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        return cap_count - sm_count

    strongest_extension = extensions[0]
    max_strength = calculate_strength(extensions[0])

    for ext in extensions[1:]:
        strength = calculate_strength(ext)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = ext

    return f"{class_name}.{strongest_extension}"
