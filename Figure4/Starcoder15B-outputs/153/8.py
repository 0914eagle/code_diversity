def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.upper()
    strength = 0
    strongest = ''
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            else:
                sm += 1
        if cap - sm > strength:
            strength = cap - sm
            strongest = extension
    return class_name + '.' + strongest

