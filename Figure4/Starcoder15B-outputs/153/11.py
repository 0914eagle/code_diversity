def Strongest_Extension(class_name, extensions):
    
    class_name = class_name.upper()
    extensions = [x.upper() for x in extensions]
    strength = []
    for ext in extensions:
        cap = 0
        sm = 0
        for char in ext:
            if char.isupper():
                cap += 1
            else:
                sm += 1
        strength.append(cap - sm)
    max_strength = max(strength)
    max_index = strength.index(max_strength)
    return class_name + '.' + extensions[max_index]

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices', 'Slices']))
print(Strongest_Extension('Slices', ['SE