
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def calculate_strength(extension: str) -> int:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        return cap_count - sm_count

    strongest_extension = None
    max_strength = float('-inf')

    for ext in extensions:
        strength = calculate_strength(ext)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = ext

    return f"{class_name}.{strongest_extension}"
