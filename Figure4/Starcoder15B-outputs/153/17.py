def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.lower()
    extensions = [x.lower() for x in extensions]
    strength = []
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength.append(cap - sm)
    max_strength = max(strength)
    max_strength_index = strength.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]

# print(Strongest_Extension('my_class