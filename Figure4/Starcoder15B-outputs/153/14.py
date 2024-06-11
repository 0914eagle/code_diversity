def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    extensions = [extension.lower() for extension in extensions]
    strength = [0] * len(extensions)
    for i in range(len(extensions)):
        for j in range(len(extensions[i])):
            if extensions[i][j].isupper():
                strength[i] += 1
            else:
                strength[i] -= 1
    max_strength = max(strength)
    max_strength_index = strength.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]


