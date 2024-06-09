
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def calculate_strength(extension: str) -> int:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        return cap_count - sm_count

    strongest_extension = extensions[0]
    strongest_strength = calculate_strength(extensions[0])

    for extension in extensions[1:]:
        strength = calculate_strength(extension)
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    return f"{class_name}.{strongest_extension}"

# Example usage
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # Output: 'my_class.AA'
