def Strongest_Extension(class_name, extensions):
    
    # your code here
    cap = 0
    sm = 0
    for i in extensions:
        for j in i:
            if j.isupper():
                cap += 1
            elif j.islower():
                sm += 1
    max_strength = cap - sm
    for i in extensions:
        cap = 0
        sm = 0
        for j in i:
            if j.isupper():
                cap += 1
            elif j.islower():
                sm += 1
        strength = cap - sm
        if strength > max_strength:
            max_strength = strength
            strongest = i
    return class_name + '.' + strongest


if