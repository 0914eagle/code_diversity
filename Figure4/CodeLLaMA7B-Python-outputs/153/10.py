def Strongest_Extension(class_name, extensions):
    
    strongest_extension = extensions[0]
    strength = 0
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            elif letter.islower():
                sm += 1
        if cap - sm > strength:
            strength = cap - sm
            strongest_extension = extension
    return class_name + '.' + strongest_extension


if