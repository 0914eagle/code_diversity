def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    class_name = class_name.upper()
    extensions = [x.lower() for x in extensions]
    extensions = [x.upper() for x in extensions]
    strengths = []
    for i in range(len(extensions)):
        strengths.append(extensions[i].count('A') - extensions[i].count('B'))
    max_strength = max(strengths)
    max_strength_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]

