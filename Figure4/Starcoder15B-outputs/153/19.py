def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    extensions = [ext.lower() for ext in extensions]
    strengths = []
    for ext in extensions:
        strength = 0
        for letter in ext:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        strengths.append(strength)
    max_strength = max(strengths)
    max_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_index]

