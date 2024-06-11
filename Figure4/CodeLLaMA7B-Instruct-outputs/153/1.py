

def Strongest_Extension(class_name, extensions):
    

    # Calculate the strength of each extension
    strengths = []
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for char in extension:
            if char.isupper():
                cap_count += 1
            elif char.islower():
                sm_count += 1
        strengths.append(cap_count - sm_count)

    # Find the strongest extension
    strongest_index = strengths.index(max(strengths))
    strongest_extension = extensions[strongest_index]

    # Return the strongest extension in the format ClassName.StrongestExtensionName
    return f"{class_name}.{strongest_extension}"


