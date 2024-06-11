def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = extensions[0]
    strongest_strength = 0
    for extension in extensions:
        strength = 0
        for letter in extension:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        if strength > strongest_strength:
            strongest = extension
            strongest_strength = strength
    return class_name + '.' + strongest


if