
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Initialize the strongest extension as the first extension in the list
    strongest_extension = extensions[0]
    # Initialize the strength of the strongest extension as the fraction of CAP - SM
    strength = len(strongest_extension) - sum(1 for c in strongest_extension if c.islower())

    # Iterate through the remaining extensions
    for extension in extensions[1:]:
        # Calculate the fraction of CAP - SM for the current extension
        current_strength = len(extension) - sum(1 for c in extension if c.islower())
        # If the current extension has a stronger strength, update the strongest extension and its strength
        if current_strength > strength:
            strongest_extension = extension
            strength = current_strength
    
    # Return the strongest extension in the format ClassName.StrongestExtensionName
    return f"{class_name}.{strongest_extension}"

