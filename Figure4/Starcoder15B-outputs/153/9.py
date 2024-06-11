def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    extensions = [x.lower() for x in extensions]
    strengths = []
    for extension in extensions:
        strength = 0
        for letter in extension:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        strengths.append(strength)
    max_strength = max(strengths)
    max_strength_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]

#