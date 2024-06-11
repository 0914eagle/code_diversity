def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest_extension = extensions[0]
    strongest_extension_strength = 0
    for extension in extensions:
        extension_strength = 0
        for letter in extension:
            if letter.isupper():
                extension_strength += 1
            elif letter.islower():
                extension_strength -= 1
        if extension_strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = extension_strength
    return class_name + '.' + strongest_extension


if