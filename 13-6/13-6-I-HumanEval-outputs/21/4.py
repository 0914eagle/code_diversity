
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Initialize the strongest extension and its strength to 0
    strongest_extension = ""
    strongest_strength = 0

    # Iterate through the list of extensions
    for extension in extensions:
        # Calculate the strength of the current extension
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())

        # If the current extension has a stronger strength than the previous strongest extension,
        # update the strongest extension and its strength
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    # Return the strongest extension in the format "ClassName.StrongestExtensionName"
    return class_name + "." + strongest_extension

