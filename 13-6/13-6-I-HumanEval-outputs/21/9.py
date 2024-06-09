
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Find the strongest extension by calculating the strength of each extension
    # and returning the extension with the highest strength
    strongest_extension = ""
    strongest_strength = 0
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        strength = cap_count - sm_count
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension
    
    # Return the strongest extension in the format ClassName.StrongestExtensionName
    return class_name + "." + strongest_extension

