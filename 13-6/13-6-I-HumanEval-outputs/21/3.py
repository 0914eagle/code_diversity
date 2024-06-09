
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    
    # Initialize the strongest extension and its strength to 0
    strongest_extension = ""
    strength = 0
    
    # Iterate through the list of extensions
    for extension in extensions:
        # Calculate the strength of the current extension
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        current_strength = cap - sm
        
        # If the current extension is stronger than the previous strongest extension,
        # set it as the new strongest extension and its strength
        if current_strength > strength:
            strongest_extension = extension
            strength = current_strength
    
    # Return the class name and the strongest extension name in the format ClassName.StrongestExtensionName
    return f"{class_name}.{strongest_extension}"

