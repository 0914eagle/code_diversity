def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    extensions = [x.lower() for x in extensions]
    strengths = []
    for ext in extensions:
        strengths.append(sum([1 if x.isupper() else -1 for x in ext]))
    max_strength = max(strengths)
    max_strength_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]

