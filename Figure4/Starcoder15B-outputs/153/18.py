def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    class_name = class_name.upper()
    class_name = class_name.capitalize()
    extensions = [x.lower() for x in extensions]
    extensions = [x.upper() for x in extensions]
    extensions = [x.capitalize() for x in extensions]
    strength = []
    for i in range(len(extensions)):
        strength.append(sum(1 for c in extensions[i] if c.isupper()) - sum(1 for c in extensions[i] if c.islower()))
    max_strength = max(strength)
    max_strength_index = [i for i, j in enumerate(strength) if j == max_strength]
    return class_name + '.' + extensions[max_strength_index[0]]

