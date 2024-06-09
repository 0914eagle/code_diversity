
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Initialize the strongest extension as the first extension in the list
    strongest_extension = extensions[0]
    # Initialize the strength of the strongest extension as the strength of the first extension
    strength = _get_strength(strongest_extension)

    # Iterate through the remaining extensions
    for extension in extensions[1:]:
        # Calculate the strength of the current extension
        current_strength = _get_strength(extension)
        # If the current extension has a stronger strength than the current strongest extension, update the strongest extension and its strength
        if current_strength > strength:
            strongest_extension = extension
            strength = current_strength

    # Return the strongest extension in the format ClassName.StrongestExtensionName
    return f"{class_name}.{strongest_extension}"

def _get_strength(extension: str) -> float:
    
    # Initialize the number of uppercase and lowercase letters in the extension's name
    cap = 0
    sm = 0

    # Iterate through the characters in the extension's name
    for char in extension:
        # If the character is uppercase, increment the number of uppercase letters
        if char.isupper():
            cap += 1
        # If the character is lowercase, increment the number of lowercase letters
        elif char.islower():
            sm += 1

    # Return the strength of the extension as the fraction CAP - SM
    return cap - sm

