def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.upper()
    max_strength = -1
    max_strength_extension = ''
    for extension in extensions:
        strength = 0
        for letter in extension:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        if strength > max_strength:
            max_strength = strength
            max_strength_extension = extension
    return class_name + '.' + max_strength_extension


