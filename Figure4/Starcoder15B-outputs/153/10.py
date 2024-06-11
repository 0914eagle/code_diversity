def Strongest_Extension(class_name, extensions):
    
    max_strength = 0
    max_strength_extension = ''
    for extension in extensions:
        strength = 0
        for char in extension:
            if char.isupper():
                strength += 1
            elif char.islower():
                strength -= 1
        if strength > max_strength:
            max_strength = strength
            max_strength_extension = extension
    return class_name + '.' + max_strength_extension

