def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.upper()
    extensions = [x.upper() for x in extensions]
    strengths = [sum([1 if x.isupper() else -1 for x in extension]) for extension in extensions]
    max_strength = max(strengths)
    max_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_index]

