

def Strongest_Extension(class_name, extensions):
    

    # Calculate the strength of each extension
    strengths = []
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        strengths.append((strength, extension))

    # Sort the strengths in descending order
    strengths.sort(reverse=True)

    # Return the strongest extension
    strongest_strength, strongest_extension = strengths[0]
    return f"{class_name}.{strongest_extension}"


