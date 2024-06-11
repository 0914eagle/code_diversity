def Strongest_Extension(class_name, extensions):
    
    # your code here
    class_name = class_name.lower()
    extensions = [x.lower() for x in extensions]
    strengths = []
    for i in extensions:
        strengths.append(sum(1 for c in i if c.isupper()) - sum(1 for c in i if c.islower()))
    max_strength = max(strengths)
    max_strength_index = strengths.index(max_strength)
    return class_name + '.' + extensions[max_strength_index]

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd', 'StuFfEd', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd', 'StuFfEd']))
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed',