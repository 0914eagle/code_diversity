
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def calculate_strength(extension: str) -> float:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        return cap_count - sm_count

    strongest_extension = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest_extension}"
